from django import forms
from .models import User

class LoginForm(forms.ModelForm):
  class Meta:
    model= User
    felids = ['email','password']
    exclude = ['name','alias']