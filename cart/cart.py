from decimal import Decimal
from django.conf import settings
from products.models import *
import uuid
from decimal import Decimal
from django.shortcuts import get_object_or_404

class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})
        self.cart = cart
        self.user = request.user if request.user.is_authenticated else None
        # Initialize user to None if not authenticated


    def add(self, request, *extra_args):
        product = extra_args[0] if extra_args else None
        product_type = extra_args[14] if len(extra_args) > 14 else None
        quantity = extra_args[1] if len(extra_args) > 1 else 1
        texture = extra_args[2] if len(extra_args) > 2 else 1
        texture_code = int(''.join(filter(str.isdigit, str(texture))))
        length = extra_args[3] if len(extra_args) > 3 else None
        width = extra_args[4] if len(extra_args) > 4 else None
        needs_curtain_rod = extra_args[5] if len(extra_args) > 5 else None
        cornice_7 = extra_args[6] if len(extra_args) > 6 else None
        cornice_9 = extra_args[7] if len(extra_args) > 7 else None
        Gordeh = extra_args[8] if len(extra_args) > 8 else None
        Miane = extra_args[9] if len(extra_args) > 9 else None
        Tasho = extra_args[10] if len(extra_args) > 10 else None
        Scouti = extra_args[11] if len(extra_args) > 11 else None
        glue_4kg = extra_args[12] if len(extra_args) > 12 else None
        glue_10kg = extra_args[13] if len(extra_args) > 13 else None
        # pricet=product.price.price_wholesale * quantity
        # print(pricet)
        if self.user and hasattr(self.user, 'customer_type'):
            customer_type = self.user.customer_type
        else:
            customer_type=None


        item_price = self.calculate_item_price(product,request, product_type, quantity, length, width,needs_curtain_rod, cornice_7, cornice_9, Gordeh, Miane, Tasho, Scouti, glue_4kg, glue_10kg,customer_type)

        existing_item = next(
            (
                item_id, item_data
            )
            for item_id, item_data in self.cart.items()
            if item_data['product_id'] == product.id and item_data['texture_code'] == texture_code
        ) if any(
            item_data['product_id'] == product.id and item_data['texture_code'] == texture_code
            for item_data in self.cart.values()
        ) else (None, None)

        if existing_item[0]:
            existing_item_id, existing_item_data = existing_item
            if existing_item_data['quantity'] is None:
                existing_item_data['quantity'] = 0  # Set to 0 if it's None
            if quantity is not None:
                existing_item_data['quantity'] += quantity
        else:
            item_id = str(uuid.uuid4())
            if quantity is None:
                quantity=1
            item_price = int(item_price)  # make sure the price is an integer
            new_item_data = {
                'product_id': product.id,
                'quantity': quantity,
                'item_price': item_price,
                'texture_code': texture_code
            }

            if product_type is not None:
                new_item_data['product_type'] = str(product_type)
            if length is not None:
                new_item_data['length'] = str(length)
            if width is not None:
                new_item_data['width'] = str(width)
            if needs_curtain_rod is not False or None:
                new_item_data['needs_curtain_rod'] = str(needs_curtain_rod)
            if cornice_7 is not None:
                new_item_data['cornice_7'] = str(cornice_7)
            if cornice_9 is not None:
                new_item_data['cornice_9'] = str(cornice_9)
            if Gordeh is not None:
                new_item_data['Gordeh'] = str(Gordeh)
            if Miane is not None:
                new_item_data['Miane'] = str(Miane)
            if Tasho is not None:
                new_item_data['Tasho'] = str(Tasho)
            if Scouti is not None:
                new_item_data['Scouti'] = str(Scouti)
            if glue_4kg is not None:
                new_item_data['glue_4kg'] = str(glue_4kg)
            if glue_10kg is not None:
                new_item_data['glue_10kg'] = str(glue_10kg)

            self.cart[item_id] = new_item_data

        print('cart:', self.cart)
        self.save()

    def save(self):
        # Save the cart and user to the session
        self.session['cart'] = self.cart
        self.session['user'] = self.user.id if self.user and self.user.is_authenticated else None
        self.session.modified = True

    def __len__(self):
        # Placeholder for getting the total number of items in the cart
        total_sum = sum(item['quantity'] for item in self.cart.values() if item['quantity'] is not None)
        return total_sum

    def remove_item(self, request, product_id):
        product_id = str(product_id)
        print('product_id', product_id)

        for item_id, item_data in list(self.cart.items()):
            if str(item_data.get('product_id')) == product_id:
                removed_product = self.cart.pop(item_id, None)  # Remove the item from the cart using its id
                if removed_product:
                    # Save the cart to the session
                    self.save()
                    print("cart", self.cart)
                    return removed_product  # Return the removed product information

        print("Item not found in the cart.")
        return None



    def update(self, product, quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            # Update the quantity of the product in the cart
            self.cart[product_id]['quantity'] = quantity
            self.save()
            # self.update_or_create_cart_item(product, quantity)

    def update_or_create_cart_item(self, request, product, quantity):
        user = request.user
        pass

    def calculate_item_price(self,product,request, product_type, quantity, length, width,needs_curtain_rod, cornice_7, cornice_9, Gordeh, Miane, Tasho, Scouti, glue_4kg, glue_10kg, customer_type):
        item_price = 0
        if self.user!= None:
            print(customer_type)
            if customer_type == 'wholesale':
                if product_type == 'Customcurtain':
                    item_price = (product.price.price_wholesale * (length * width)) * quantity
                elif product_type == 'cornice':
                    price_Cornic_7 = product.Cornic_7.price_wholesale * cornice_7 if cornice_7 is not None else 0
                    price_Cornic_9 = product.Cornic_9.price_wholesale * cornice_9 if cornice_9 is not None else 0
                    price_Gordeh = product.Gordeh.price_wholesale * Gordeh if Gordeh is not None else 0
                    price_Miane = product.Miane.price_wholesale * Miane if Miane is not None else 0
                    price_Tasho = product.Tasho.price_wholesale * Tasho if Tasho is not None else 0
                    price_Scouti = product.Scouti.price_wholesale * Scouti if Scouti is not None else 0
                    item_price = price_Cornic_7 + price_Cornic_9 + price_Gordeh + price_Miane + price_Tasho + price_Scouti
                elif product_type == 'Floorcoverings':
                    price_glue_4kg = product.glue_4kg.price_wholesale * glue_4kg if glue_4kg is not None else 0
                    price_glue_10kg = product.glue_10kg.price_wholesale * glue_10kg if glue_10kg is not None else 0
                    price_Floorcoverings = product.price.price_wholesale * quantity
                    item_price = price_glue_4kg + price_glue_10kg + price_Floorcoverings
                else:
                    item_price = product.price.price_wholesale * quantity
            else:
                if product_type == 'Customcurtain':
                    item_price = (product.price.price_retail * (length * width)) * quantity+(needs_curtain_rod*quantity)
                elif product_type == 'cornice':
                    price_Cornic_7 = product.Cornic_7.price_retail * cornice_7 if cornice_7 is not None else 0
                    price_Cornic_9 = product.Cornic_9.price_retail * cornice_9 if cornice_9 is not None else 0
                    price_Gordeh = product.Gordeh.price_retail * Gordeh if Gordeh is not None else 0
                    price_Miane = product.Miane.price_retail * Miane if Miane is not None else 0
                    price_Tasho = product.Tasho.price_retail * Tasho if Tasho is not None else 0
                    price_Scouti = product.Scouti.price_retail * Scouti if Scouti is not None else 0
                    item_price = price_Cornic_7 + price_Cornic_9 + price_Gordeh + price_Miane + price_Tasho + price_Scouti
                elif product_type == 'Floorcoverings':
                    price_glue_4kg = product.glue_4kg.price_retail * glue_4kg if glue_4kg is not None else 0
                    price_glue_10kg = product.glue_10kg.price_retail * glue_10kg if glue_10kg is not None else 0
                    price_Floorcoverings = product.price.price_retail * quantity
                    item_price = price_glue_4kg + price_glue_10kg + price_Floorcoverings
                else:
                    item_price = product.price.price_retail * quantity
        else:
                if product_type == 'Customcurtain':
                    item_price = (product.price.price_retail * (length * width)) * quantity+(needs_curtain_rod*quantity)
                elif product_type == 'cornice':
                    price_Cornic_7 = product.Cornic_7.price_retail * cornice_7 if cornice_7 is not None else 0
                    price_Cornic_9 = product.Cornic_9.price_retail * cornice_9 if cornice_9 is not None else 0
                    price_Gordeh = product.Gordeh.price_retail * Gordeh if Gordeh is not None else 0
                    price_Miane = product.Miane.price_retail * Miane if Miane is not None else 0
                    price_Tasho = product.Tasho.price_retail * Tasho if Tasho is not None else 0
                    price_Scouti = product.Scouti.price_retail * Scouti if Scouti is not None else 0
                    item_price = price_Cornic_7 + price_Cornic_9 + price_Gordeh + price_Miane + price_Tasho + price_Scouti
                elif product_type == 'Floorcoverings':
                    price_glue_4kg = product.glue_4kg.price_retail * glue_4kg if glue_4kg is not None else 0
                    price_glue_10kg = product.glue_10kg.price_retail * glue_10kg if glue_10kg is not None else 0
                    price_Floorcoverings = product.price.price_retail * quantity
                    item_price = price_glue_4kg + price_glue_10kg + price_Floorcoverings
                else:
                    item_price = product.price.price_retail * quantity
            

        return item_price

    def get_total_price(self):
        # Placeholder for getting the total price of all items in the cart
        total_price = sum(
            int(item['item_price'])  for item in self.cart.values()
        )
        return total_price

    def clear(self):
        # Clear the cart
        self.cart = {}
        self.save()

    def __iter__(self):
        for item_id, item_data in self.cart.items():
            product_id = item_data.get('product_id', None)
            
            if product_id:
                product = get_object_or_404(Product, pk=product_id)

                # Get the selected texture for the item
                texture_code = item_data.get('texture_code', None)
                selected_texture = product.get_selected_texture(texture_code) if texture_code else None
                texture_image_url = selected_texture.image.url if selected_texture and selected_texture.image else None
                quantity = item_data.get('quantity', 1)  # Set default quantity to 1 if it's None
                item_price = item_data.get('item_price', 0)

                # Convert Decimal values to float for JSON serialization

                yield {
                    'product': product,
                    'quantity': item_data['quantity'],
                    'product_code': product.product_code,
                    'product_length': product.dimensions.length if product.dimensions else None,
                    'product_width': product.dimensions.width if product.dimensions else None,
                    'description': product.description,
                    'image_url': product.images.first().image.url if product.images.exists() else None,
                    'texture_code': texture_code,  # Include the texture code
                    'texture_image_url': texture_image_url,
                    'item_price': item_data.get('item_price'),
                    'length': item_data.get('length'),  # Include length if available
                    'product_type': item_data.get('product_type'),  # Include product_type if available
                    'width': item_data.get('width'),    # Include width if available
                    'number_of_panels': item_data.get('number_of_panels'),  # Include number_of_panels if available
                    'needs_curtain_rod': item_data.get('needs_curtain_rod'),  # Include needs_curtain_rod if available
                    'cornice_7': item_data.get('cornice_7'),  # Include cornice_7 if available
                    'cornice_9': item_data.get('cornice_9'),  # Include cornice_9 if available
                    'Gordeh': item_data.get('Gordeh'),  # Include Gordeh if available
                    'Miane': item_data.get('Miane'),  # Include Miane if available
                    'Tasho': item_data.get('Tasho'),  # Include Tasho if available
                    'Scouti': item_data.get('Scouti'),  # Include Scouti if available
                    'glue_4kg': item_data.get('glue_4kg'),  # Include glue_4kg if available
                    'glue_10kg': item_data.get('glue_10kg'),  # Include glue_10kg if available
                }



    def get_price_for_product(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            # Get the price and quantity for the specified product
            price = Decimal(self.cart[product_id]['price'])
            quantity = self.cart[product_id]['quantity']

            # Calculate the total price for the product
            total_price_for_product = price * quantity
            return total_price_for_product
        else:
            return Decimal('0')
        
    def split_string_to_dict(input_str, separator=' '):
        parts = input_str.split(separator)
        if len(parts) >= 2:
            result_dict = {
                parts[0]: ' '.join(parts[1:]).strip(),
            }
            return result_dict
        else:
            print("Invalid input. The input should have at least two parts.")
            return None
        
    def get_price_for_product(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            # Get the quantity for the specified product
            quantity = self.cart[product_id]['quantity']
            return quantity
        else:
            return 0
        
    def get_texture(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            # Get the texture code for the specified product
            texture_code = self.cart[product_id].get('texture_code', None)
            return texture_code
        else:
            return None
        

