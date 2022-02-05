# App/Models/User_forms.py

# Django modules
from django import forms

# Locals

# Create your form here.


# MODEL FORM: SignUpForm
class SignUpForm(forms.Form):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    user = forms.CharField(label='Usuiario')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)