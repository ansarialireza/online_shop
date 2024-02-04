from django.urls import path
from .views import *

app_name = 'payments'

urlpatterns = [
    path('go_to_gatway', go_to_gateway_view, name='payment'),
    path('callback', callback_gateway_view, name='callback'),
]
