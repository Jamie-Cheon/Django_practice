from django import forms
from django.contrib.auth.hashers import check_password
from .models import User 


class RegisterForm(forms.Form):
  email = forms.EmailField(
    error_messages={
      'required': 'Please enter your email.'
    },
    max_length=64, label='Email'
  )

  password = forms.CharField(
    error_messages={
      'required': 'Please enter your password.'
    },
    widget=forms.PasswordInput, label='Password'
  )

  re_password = forms.CharField(
    error_messages={
      'required': 'Password does not match.'
    },
    widget=forms.PasswordInput, label='Confirm Password'
  )

  def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data.get('email')
    password = cleaned_data.get('password')
    re_password = cleaned_data.get('re_password')

    if password and re_password:
      if password != re_password:
        self.add_error('re_password', 'Password Does Not match')



class LoginForm(forms.Form):
  email = forms.EmailField(
    error_messages={
      'required': 'Please enter your email.'
    },
    max_length=64, label='Email'
  )

  password = forms.CharField(
    error_messages={
      'required': 'Please enter your password.'
    },
    widget=forms.PasswordInput, label='Password'
  )


  def clean(self):    

    # call clean() method that already exists inside form object
    # error when 1st check(clean()) failed 
    cleaned_data = super().clean()   
    email = cleaned_data.get('email')
    password = cleaned_data.get('password')

    # after success clean() method
    if email and password:  
      try:
        user = User.objects.get(email=email)
      except user.DoesNotExist:
        self.add_error('email', 'Email Does Not Exist')
        return
      if not check_password(password, user.password):    # if password unmatch
        self.add_error('password', 'Password Does Not Match')
