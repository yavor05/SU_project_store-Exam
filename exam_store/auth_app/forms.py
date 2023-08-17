from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError

from .models import UserProfile


class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'gender', 'age']

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'username_exists': "A user with this username already exists.",
        'invalid_email': "Please enter a valid email address.",
    }

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username=username).exists():
            raise ValidationError(self.error_messages['username_exists'])
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise ValidationError(self.error_messages['invalid_email'])
        return email


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,
                                                           "placeholder": "Username"}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        "autocomplete": "current-password", "placeholder": "Password"
    }))


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'gender', 'email']
        exclude = ['password']
