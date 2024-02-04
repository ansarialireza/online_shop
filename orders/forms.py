from django import forms

class OrderCreateForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label='نام')
    lastname = forms.CharField(max_length=255, required=True, label='نام خانوادگی')
    address = forms.CharField(widget=forms.Textarea, required=True, label='آدرس')
    postal_code = forms.CharField(max_length=10, required=True, label='کد پستی')
    city = forms.CharField(max_length=255, required=True, label='شهر')
    province = forms.CharField(max_length=255, required=True, label='استان')
