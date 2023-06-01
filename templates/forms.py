from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username =  forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(LoginForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()


class ResetPasswordForm(LoginForm):
    set_password = forms.CharField(max_length=64)
    repeat_set_password = forms.CharField(widget=forms.PasswordInput)