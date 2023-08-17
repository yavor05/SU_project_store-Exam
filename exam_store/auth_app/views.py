from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from exam_store.auth_app.forms import UserProfileForm, LoginForm, UserProfileEditForm
from exam_store.auth_app.models import UserProfile
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, "Username or/and password is incorrect")

    context = {}
    return render(request, template_name='auth_app/login_page.html', context=context)


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


def register_view(request):
    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get("username")
            messages.success(request, "Account was created with username: " + user_name)
            return redirect('login_page')

    context = {
        'form': form

    }
    return render(request, template_name='auth_app/register_page.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login_page')


class UserEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = "auth_app/edit_profile.html"

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})
