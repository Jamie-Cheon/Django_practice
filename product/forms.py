from django import forms
from .models import Product

class RegisterForm(forms.Form):
  name = forms.CharField(
    error_messages={
      'required': 'Please enter product name'
    },
    max_length=64, label='Name'
  )

  price = forms.IntegerField(
    error_messages={
      'required': 'Please enter product price'
    },
    label='Price'
  )

  description = forms.CharField(
    error_messages={
      'required': 'Please enter product description'
    }, 
    label='Description'
  )

  stock = forms.IntegerField(
    error_messages={
      'required': 'Please enter product stock'
    },
    label='Stock'
  )

  def clean(self):
    cleaned_data = super().clean()
    name = cleaned_data.get('name')
    price = cleaned_data.get('price')
    description = cleaned_data.get('description')
    stock = cleaned_data.get('stock')

    if not(name and price and description and stock):
      self.add_error('name', 'Please fill out empty space')
