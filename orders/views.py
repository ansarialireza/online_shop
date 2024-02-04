from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model  # Import get_user_model
from cart.cart import Cart
from .models import *
from products.models import Product

class OrderCreateView(View):
    template_name = 'path_to_your_template/order_create.html'  # Provide the actual path

    def get(self, request, *args, **kwargs):
        # Optionally, you can implement a GET method to render a confirmation page
        # This is useful if you want users to confirm their order before placing it
        # cart = Cart(request)
        # order_items = [
        #     {
        #         'product': item['product'],
        #         'quantity': item['quantity'],
        #         'texture_code': item['texture_code'],
        #         'price': item['price'],
        #         'total_price': item['quantity'] * item['price'],
        #     }
        #     for item in cart
        # ]
        # total_price = cart.get_total_price()

        # context = {
        #     'order_items': order_items,
        #     'total_price': total_price,
        # }
        # return render(request, self.template_name, context)
        return redirect('website:home')  # Replace 'website:home' with your actual home URL
    

    def post(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            messages.error(request, 'برای ثبت سفارش، لطفاً ابتدا وارد حساب کاربری خود شوید.')
            return redirect('path_to_login')  # Replace 'path_to_login' with your actual login URL

        # Check if the user's profile information is complete
        required_fields = ['name', 'lastname', 'address', 'postal_code', 'city', 'province']
        user_model = get_user_model()  # Get the User model dynamically
        if not all(getattr(request.user, field) for field in required_fields):
            messages.error(request, 'لطفاً اطلاعات حساب خود را کامل کنید تا بتوانید سفارش دهید.')
            return redirect('accounts:update')  # Replace 'accounts:update' with your actual profile update URL

        # Create a new order
        order = Order.objects.create(user=request.user)

        # Add items to the order
        cart = Cart(request)
        order_items = []

        for cart_item in cart:
            product = cart_item['product']
            product_type = cart_item['product_type']
            quantity = cart_item['quantity']
            texture_code = cart_item['texture_code']
            length = cart_item['length']
            width = cart_item['width']
            needs_curtain_rod = cart_item['needs_curtain_rod']
            cornice_7 = cart_item['cornice_7']  
            cornice_9 = cart_item['cornice_9']  
            Gordeh = cart_item['Gordeh']  
            Miane = cart_item['Miane']  
            Tasho = cart_item['Tasho']  
            Scouti = cart_item['Scouti']  
            glue_4kg = cart_item['glue_4kg']  
            glue_10kg = cart_item['glue_10kg']  


            if product_type=='cornice':
                order_item = Cornice.objects.create(
                order=order,
                product=product,
                texture_code=texture_code,
                cornice_7=cornice_7,  
                cornice_9=cornice_9,  
                Gordeh=Gordeh,  
                Miane=Miane,  
                Tasho=Tasho,  
                Scouti=Scouti,  
                )
            elif product_type=='Customcurtain':
                order_item = Customcurtain.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                texture_code=texture_code,
                length=length,
                width=width,
                needs_curtain_rod=needs_curtain_rod,
                )
            elif product_type=='Floorcoverings':
                order_item = Floorcoverings.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                texture_code=texture_code, 
                glue_4kg=glue_4kg,  
                glue_10kg=glue_10kg,  
                )
            else:
                order_item = NormalProducts.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                texture_code=texture_code,
                )
            # order_item = OrderItem.objects.create(
            #     order=order,
            #     product=product,
            #     quantity=quantity,
            #     texture_code=texture_code,
            #     length=length,
            #     width=width,
            #     needs_curtain_rod=needs_curtain_rod,
            #     cornice_7=cornice_7,  
            #     cornice_9=cornice_9,  
            #     Gordeh=Gordeh,  
            #     Miane=Miane,  
            #     Tasho=Tasho,  
            #     Scouti=Scouti,  
            #     glue_4kg=glue_4kg,  
            #     glue_10kg=glue_10kg,  
            # )

            # order_items.append({
            #     'product': product,
            #     'quantity': quantity,
            #     'texture_code': texture_code,
            #     'length': length,
            #     'width': width,
            #     'number_of_panels': cart_item.get('number_of_panels'),
            #     'needs_curtain_rod': needs_curtain_rod,
            #     'cornice_7': cornice_7,  
            #     'cornice_9': cornice_9,  
            #     'Gordeh': Gordeh,  
            #     'Miane': Miane,  
            #     'Tasho': Tasho,  
            #     'Scouti': Scouti,  
            #     'glue_4kg': glue_4kg,  
            #     'glue_10kg': glue_10kg,  
            # })

        # Clear the shopping cart
        cart.clear()
        cart.save()
        # Optionally, you can pass order details to the success page
        messages.success(request, 'سفارش با موفقیت ثبت شد')
        # return render(request, 'order_success.html', context)
        return redirect('website:home')  # Replace 'website:home' with your actual home URL

