from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class LoginPageView(LoginView):
    template_name = "auth_app/login_page.html"


class RegisterPageView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth_app/register_page.html'
    success_url = reverse_lazy('home_page')
