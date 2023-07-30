from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView

from exam_store.auth_app.models import UserProfile


class LoginPageView(LoginView):
    template_name = "auth_app/login_page.html"


class RegisterPageView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth_app/register_page.html'
    success_url = reverse_lazy('home_page')


class ProfileDetailsView(DetailView):
    model = UserProfile
    template_name = 'auth_app/profile_details.html'
    context_object_name = 'user_profile'


class CreateUserProfileView(CreateView):
    model = UserProfile
    template_name = 'auth_app/register_page.html'
    fields = ['description', 'avatar', 'age', 'name']  # Specify the fields you want to include in the form
    success_url = reverse_lazy('profile_details')  # Redirect to the profile details page upon successful creation

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
