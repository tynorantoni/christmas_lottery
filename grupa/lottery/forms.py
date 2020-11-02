from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="imię (z dużej literki ;))")
    password = forms.CharField(label="hasło", widget=forms.PasswordInput)
