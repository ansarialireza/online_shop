from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add'),
    path('addcustomcurtain/<int:product_id>/', AddCustomCurtainToCartView.as_view(), name='addcustomCurtain'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove'),  
    path('update/<int:product_id>/', UpdateCartView.as_view(), name='update'),
]
