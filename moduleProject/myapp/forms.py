from django import forms
from django.forms import ModelForm
from django.http import request

from myapp.models import MyUser, Product, Purchase, PurchaseReturns


class UserForm(ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password_confirmation',)

    def clean(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords do not match!')
        return data


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity_in_stock',)


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity_of_products',)


class PurchaseReturnForm(ModelForm):
    class Meta:
        model = PurchaseReturns
        fields = []
