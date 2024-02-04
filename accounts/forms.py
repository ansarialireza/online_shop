# accounts/forms.py

from django import forms
from .models import *
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'lastname', 'phone_number', 'postal_code', 'province', 'city', 'address')

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'postal_code', 'province', 'city', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields if needed




class SignUpwholesaleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'phone_number', 'postal_code', 'province', 'city', 'address', 'customer_type','is_hurry','store_phone','store_card','photo_of_the_store','business_license']

class UpdatewholesaleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname','postal_code', 'province', 'city', 'address', 'customer_type','is_hurry','store_phone','store_card','photo_of_the_store','business_license']

