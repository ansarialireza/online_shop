from django.urls import path
from .views import OrderCreateView

app_name = 'orders'


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    # Add more views/urls as needed
]










# # orders/urls.py
# from django.urls import path
# from .views import OrderView, PaymentView, OrderSuccessView

# app_name = 'orders'

# urlpatterns = [
#     path('create/', OrderView.as_view(), name='create_order'),
#     path('<int:order_id>/payment/', PaymentView.as_view(), name='payment'),
#     path('<int:order_id>/success/', OrderSuccessView.as_view(), name='order_success'),
# ]
