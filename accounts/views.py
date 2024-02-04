from datetime import datetime, timedelta
import json
import random
from django.shortcuts import render, redirect
from django.contrib.auth import login,get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.cache import cache
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views import View
from kavenegar import KavenegarAPI, APIException, HTTPException
from .forms import *
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

class SendVerificationCodeView(View):
    def generate_random_code(self, phone_number):
        verification_code = str(random.randint(1000, 9999))
        cache_key = f'verification_code:{phone_number}'
        print(cache_key)
        cache.set(cache_key, {'code': verification_code,'phone_number':phone_number, 'timestamp': datetime.now()})

        return verification_code

    def send_sms(self, phone_number, verification_code):
        api_key = '2F4C64566E467667592B6C774838646B37546D526E734D457738377669417345474D687778487A6E44314D3D'  # Replace with your actual API key
        sender_id = '1000689696'  # Replace with your actual sender ID

        try:
            api = KavenegarAPI(api_key)
            params = {
                'sender': sender_id,
                'receptor': phone_number,
                'message': f'Your verification code is: {verification_code}',
            }

            response = api.sms_send(params)
            print(response)
            if response['return']['status'] == 200:
                return {'success': True}
            else:
                return {'success': False, 'error': f'Failed to send SMS. Status: {response["return"]["status"]}, Message: {response["return"]["message"]}'}
    
        except (APIException, HTTPException) as e:
            return {'success': False, 'error': f'Failed to send SMS: {e}'}

    def send_verification_code(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})

        phone_number = data.get('phone_number')
        
        print(phone_number)
        cache_key = f'verification_code:{phone_number}'

        cache_data = cache.get(cache_key)
        if cache_data and datetime.now() - cache_data['timestamp'] <= timedelta(minutes=2):
            return JsonResponse({'error': 'Code already sent. Please wait before requesting a new one.'})

        print('Generate and send a new code')
        verification_code = self.generate_random_code(phone_number)
        print(verification_code)
        sms_result = self.send_sms(phone_number, verification_code)
        print(sms_result)
        if sms_result['success']:
            return JsonResponse({'message': 'Verification code sent successfully'})
        else:
            return JsonResponse({'error': sms_result['error']})

    def post(self, request, *args, **kwargs):
        return self.send_verification_code(request)


class LoginWithConfirmationCodeView(View):

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})

        # Clear the session cart when a user logs in
        request.session.pop('cart', None)

        # Initialize a new cart for the logged-in user
        user_cart = Cart(request)
        print(f"Before saving: {user_cart.cart}")
        user_cart.save()
        print(f"After saving: {user_cart.cart}")
        print(f"User associated with the cart: {user_cart.user}")

        confirmation_code = data.get('confirmation_code')
        phone_number = data.get('phone_number')

        cache_key = f'verification_code:{phone_number}'
        cache_data = cache.get(cache_key)

        print(f"Received confirmation code: {confirmation_code}")
        # print(f"Cache data: {cache_data}")

        if cache_data and cache_data['code'] == confirmation_code:
            user = get_user_model().objects.filter(phone_number=phone_number).first()

            if not user:
                try:
                    new_user = get_user_model().objects.create(phone_number=phone_number, password=make_password(confirmation_code))
                    new_user.is_active = True
                    new_user.save()

                    messages.success(request, 'ثبت نام اولیه با موفقیت انجام شد ، شما وارد شدید')

                    login(request, new_user, backend='accounts.backends.CustomUserBackend')  

                    # print(f"User registered and logged in: {new_user.phone_number}")

                    return JsonResponse({'message': 'Registration successful. You are now logged in.'})
                except IntegrityError:
                    messages.error(request, 'User with this phone number already exists. Please log in.')
                    # print(f"User creation failed. User with phone number {phone_number} already exists.")

                    return JsonResponse({'error': 'User creation failed. User with this phone number already exists.'})
            else:

                # print(f"User already registered: {user.phone_number}")
                login(request, user, backend='accounts.backends.CustomUserBackend') 
                messages.success(request,f"شما با شماره {user.phone_number} وارد سایت شدید")
                
                return JsonResponse({'message': 'User is already registered. Please log in.'})
        else:
            messages.error(request, 'کد تایید اشتباه است ')

            print("Invalid confirmation code.")

            return JsonResponse({'error': 'Invalid confirmation code'})

class CustomerSignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(None)
            user.is_active = True
            user.save()
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد. خوش آمدید!')
            return redirect('website:home')
            # return render(request, self.template_name, {'form': form, 'phone_number': phone_number, 'user': user})
        else:
            messages.error(request, 'فرم نامعتبر است. لطفاً اصلاحات لازم را انجام دهید.')
            print('form is not valid')
            if 'phone_number' in form.errors:
                messages.error(request, 'شماره تلفن تکراری است. لطفاً از شماره تلفن دیگری استفاده کنید.')

        return render(request, self.template_name, {'form': form})



@method_decorator(login_required, name='dispatch')
class UpdateUserView(LoginRequiredMixin, View):
    template_name = 'registration/update_user.html'

    def get(self, request):
        form = UpdateUserForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات کاربری با موفقیت بروزرسانی شد.')
            return redirect('website:home')  # Replace 'profile' with the actual URL name for the user profile
        else:
            messages.error(request, 'فرم نامعتبر است. لطفاً اصلاحات لازم را انجام دهید.')
            return render(request, self.template_name, {'form': form})
        

class WholesaleCustomerView(View):
    template_name = 'registration/wholesaleSignUp.html' 

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpwholesaleForm(request.POST, request.FILES)
        # Debugging print statements
        print(f"Form data: {request.POST}")

        if form.is_valid():
            is_hurry = form.cleaned_data.get('is_hurry')
            
            if is_hurry:
                instance = form.save(commit=False)
                instance.customer_type = 'retail'
                instance.save()
                messages.success(request, 'ثبت نام شما با موفقیت انجام شد، لطفا خرید خود را انجام دهید ، همکاران ما به زودی با شما تماس خواهند گرفت ')
                return redirect('/')

            else:

                messages.success(request, 'ثبت نام با موفقیت انجام شد ، پس از تایید مدارک حساب کاربری شما فعال خواهد شد')
                return redirect('/')
        else:
            if 'phone_number' in form.errors:
                messages.error(request, 'شماره تلفن تکراری است. لطفاً از شماره تلفن دیگری استفاده کنید.')
                return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class WholesaleCustomerUpdateView(View):
    template_name = 'registration/update_wholesaleSignUp.html'

    def get(self, request):
        form = UpdatewholesaleForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UpdatewholesaleForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات کاربری با موفقیت بروزرسانی شد.')
            return redirect('website:home')  # Replace 'profile' with the actual URL name for the user profile
        else:
            messages.error(request, 'فرم نامعتبر است. لطفاً اصلاحات لازم را انجام دهید.')
            return render(request, self.template_name, {'form': form})
        
class LogoutView(View):
    def get(self, request, *args, **kwargs):
          # Clear the cart from the session
        request.session.pop('cart', None)
        logout(request)
        messages.success(request,'از حساب کاربری خود خارج شدید')
        return redirect('/')