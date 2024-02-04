# accounts/urls.py
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('send_verification_code/', SendVerificationCodeView.as_view(), name='send_verification_code'),
    path('login_with_confirmation_code/', LoginWithConfirmationCodeView.as_view(), name='login_with_confirmation_code'),
    # path('logout/', logout_view, name='logout'),
    path('signup/', CustomerSignUpView.as_view(), name='signup'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path('Partnersignup/', WholesaleCustomerView.as_view(), name='PartnerSignUp'),
    path('Partnerupdate/', WholesaleCustomerUpdateView.as_view(), name='Partnerupdate'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
