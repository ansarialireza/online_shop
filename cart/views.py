# cart/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from .forms import *
from products.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from orders.models import Order 
from .cart import Cart
from products.views import ProductDetailView
# from .models import CartItem

class CartView(View):
    template_name = 'cart/cart.html'

    def get(self, request):
        cart = Cart(request)
        # cart.clear()
        context = {
            'cart': cart,  # Pass the entire cart object to the template
        }
        return render(request, self.template_name, context)

class AddToCartView(View):
    template_name = 'products/product_detail/product_detail.html'

    def post(self, request, product_id):
        products = get_object_or_404(Product, pk=product_id)
        form = AddToCartForm(request.POST)

        product_detail=ProductDetailView()
        product_type,product=product_detail.get_class_name_for_record(product_id)

        if product== None :
            # print('product is ::::',product)
            product=products
        # print("Raw Form Data:", request.POST)  # Print raw form data for debugging
        # # Debugging: Print form data before validation
        # print("Quantity:", form.data.get('quantity'))
        # print("Texture Code:", form.data.get('texture_code'))

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            texture_code = form.cleaned_data['texture_code']
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            needs_curtain_rod = form.cleaned_data['needs_curtain_rod']
            cornice_7 = form.cleaned_data['cornice_7']
            cornice_9 = form.cleaned_data['cornice_9']
            Gordeh = form.cleaned_data['Gordeh']
            Miane = form.cleaned_data['Miane']
            Tasho = form.cleaned_data['Tasho']
            Scouti = form.cleaned_data['Scouti']
            glue_4kg = form.cleaned_data['glue_4kg']
            glue_10kg = form.cleaned_data['glue_10kg']

            # print(length,width,needs_curtain_rod)
            # print(cornice_7,cornice_9,Gordeh,Miane,Tasho,Scouti)
            cart = Cart(request)
            cart.add(
                request,
                product,
                quantity,
                texture_code,
                length,
                width,
                needs_curtain_rod,
                cornice_7,
                cornice_9,
                Gordeh,
                Miane,
                Tasho,
                Scouti,
                glue_4kg,
                glue_10kg,
                product_type,
            )

            messages.success(request, f" محصول با تکسچر {texture_code} به سبد خرید شما اضافه شد.")
            return redirect('cart:cart')
        else:
            print("Invalid Form Data:", form.errors)  # Print form errors for debugging
            # return redirect('products:product_detail')
            messages.warning(request, "شما اطلاعات را درست وارد نکرده اید")

            return redirect('products:cornice')
        



class RemoveFromCartView(View):
    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        removed_product=cart.remove_item(request, product_id)
        print('removed_product',removed_product)
        if removed_product:
            messages.success(request,"یک محصول از سبد شما حذف شد")
        else:
            messages.warning(request, "محصول از سبد شما حذف نشد")

        return redirect('cart:cart')

class UpdateCartView(View):
    template_name = 'cart/update_cart.html'

    def get_class_name_for_record(self,record_id):
        # try:
        #     product = Product.objects.get(id=record_id)
        #     return 'Product'
        # except Product.DoesNotExist:
        #     pass

        try:
            cornice = Cornice.objects.get(id=record_id)
            return 'cornice'
        except Cornice.DoesNotExist:
            pass

        try:
            custom_curtain = Customcurtain.objects.get(id=record_id)
            return 'Customcurtain'
        except Customcurtain.DoesNotExist:
            pass
        # If the record is not found in any class
        return None

    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        initial_quantity = cart.get_price_for_product(product)
        initial_texture = cart.get_texture(product)  # Add method to get selected texture
        class_name =class_name = self.get_class_name_for_record(product_id)


        form = UpdateCartForm(initial={'quantity': initial_quantity, 'texture': initial_texture})

        context = {
            'form': form,
            'product': product,
            'class_name': class_name,
        }

        return render(request, self.template_name, context)

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)

        form = UpdateCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            texture = form.cleaned_data['texture']

            # Check if the product is a custom curtain or a general product
            if product.is_custom_curtain:
                # Update custom curtain information
                cart.update_custom_curtain(product, quantity, texture)
            else:
                # Update general product information
                cart.update(product, quantity, texture=texture)

            messages.success(request, f"تغییرات به سبد خرید شما اعمال شد.")
            return redirect('cart:cart')

        context = {
            'form': form,
            'product': product,
        }

        return render(request, self.template_name, context)
    





class AddCustomCurtainToCartView(View):
    template_name = 'products/product_detail/product_detail.html'

    def post(self, request, product_id):
        cart = Cart(request)  # Ensure that you are correctly initializing the Cart object
        product = get_object_or_404(Product, pk=product_id)
        form = CustomCurtainForm(request.POST)
        context = {'product': product}

        if form.is_valid():
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            number_of_panels = form.cleaned_data['number_of_panels']
            needs_curtain_rod = form.cleaned_data['needs_curtain_rod']

            custom_curtain_product = Customcurtain(
                title=product.title,
                category=product.category,
                price=product.price,
                dimensions=product.dimensions,
                curtain_rod=True,
                curtain_model="Your Model",
                side_fabric="Your Fabric",
            )

            # Add custom_curtain_product to the cart
            custom_curtain_info={'length': length,'width': width,'number_of_panels': number_of_panels,'needs_curtain_rod': needs_curtain_rod,}
            cart.add_custom_curtain(request,custom_curtain_product,1,custom_curtain_info)
            messages.success(request, "پرده سفارشی به سبد خرید شما اضافه شد.")
            return redirect('cart:cart')
        else:
            messages.error(request, "لطفاً اطلاعات معتبر وارد کنید.")
            return render(request, self.template_name, context)



class FinalizeOrderView(View):
    template_name = 'cart/finalize_order.html'

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        cart = Cart(request)

        # Additional logic to handle order finalization
        # You can create an Order instance and associate it with the user

        # For example:
        order = Order.objects.create(user=request.user, total_amount=cart.get_total())
        for item in cart:
            product = get_object_or_404(Product, pk=item['product_id'])
            quantity = item['quantity']
            order.items.create(product=product, quantity=quantity)

        # Clear the cart after finalizing the order
        cart.clear()

        context = {
            'order': order,
        }

        return render(request, self.template_name, context)