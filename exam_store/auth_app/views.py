from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView

from exam_store.auth_app.forms import UserProfileForm, LoginForm
from exam_store.auth_app.models import UserProfile


class LoginPageView(LoginView):
    template_name = "auth_app/login_page.html"
    form_class = LoginForm
    next_page = reverse_lazy('home_page')

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


class ProfileDetailsView(DetailView):
    model = UserProfile
    template_name = 'auth_app/profile_details.html'
    context_object_name = 'user_profile'

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


class UserRegisterView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'auth_app/register_page.html'
    success_url = reverse_lazy('home_page')

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


class LogoutPageView(LogoutView):
    next_page = reverse_lazy("login_page")

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)
