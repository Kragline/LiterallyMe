from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


username_attrs = {'type': 'text', 'class': 'form-control', 'placeholder': 'Username'}
email_attrs = {'type': 'email', 'class': 'form-control', 'placeholder': 'name@example.com'}
password_attrs = {'type': 'password', 'class': 'form-control', 'placeholder': 'Username'}


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=username_attrs))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=email_attrs))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=password_attrs))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs=password_attrs))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=password_attrs))
