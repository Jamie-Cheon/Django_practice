from django import forms
from django.db import transaction
from .models import Order
from product.models import Product
from user.models import User


class RegisterForm(forms.Form):
  def __init__(self, request, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.request = request


  quantity = forms.IntegerField(
    error_messages={
      'required': 'Please enter product quantity'
    },
    label='quantity'
  )

  product = forms.IntegerField(
    error_messages={
      'required': 'Please enter product'
    }, 
    label='Product', widget=forms.HiddenInput
  )


  def clean(self):
    cleaned_data = super().clean()
    quantity = cleaned_data.get('quantity')
    product = cleaned_data.get('product')

    if not(quantity and product):
      self.add_error('quantity', 'Please enter quantity.')