from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="mail")
    password = forms.CharField(label="hasło", widget=forms.PasswordInput)
