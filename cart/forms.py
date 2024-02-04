# cart/forms.py

from django import forms

class CustomCurtainForm(forms.Form):
    length = forms.DecimalField(label='طول', min_value=0, required=True)
    width = forms.DecimalField(label='عرض', min_value=0, required=True)
    number_of_panels = forms.IntegerField(label='تعداد پنل', min_value=1, required=True)
    needs_curtain_rod = forms.BooleanField(label='نیاز به چوب پرده', required=False)

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تعداد'}))
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    price = forms.IntegerField(required=False,widget=forms.HiddenInput(),initial=0 )
    length = forms.DecimalField(required=False)
    width = forms.DecimalField(required=False)
    number_of_panels = forms.IntegerField(required=False)
    needs_curtain_rod = forms.BooleanField(required=False)
    texture_code = forms.CharField(max_length=50, widget=forms.HiddenInput())
    cornice_7 = forms.DecimalField(required=False,)
    cornice_9 = forms.DecimalField(required=False,)
    Gordeh = forms.DecimalField(required=False,)
    Miane = forms.DecimalField(required=False,)
    Tasho = forms.DecimalField(required=False,)
    Scouti = forms.DecimalField(required=False,)
    glue_4kg = forms.DecimalField(required=False,)
    glue_10kg = forms.DecimalField(required=False,)


    custom_curtain_form = CustomCurtainForm()

class UpdateCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=100,  # Adjust the maximum value as needed
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
