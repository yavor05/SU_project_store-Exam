from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from .models import UserProfile


class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,
                                                           "placeholder": "Username"}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        "autocomplete": "current-password", "placeholder": "Password"
    }))
