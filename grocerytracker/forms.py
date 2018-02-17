from django import forms


class ProductForm(forms.Form):
    product = forms.CharField(label='Product', max_length=255)
    price = forms.DecimalField(label='Price')
    store = forms.CharField(label='Store', max_length=255)
