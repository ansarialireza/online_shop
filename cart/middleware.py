# cart/middleware.py
from .cart import Cart

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Load the cart from the session
        cart = Cart(request)
        request.cart = cart

        response = self.get_response(request)

        # Save the cart to the session
        cart.save()

        return response
