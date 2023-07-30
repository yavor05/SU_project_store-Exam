from django.urls import path
from .views import LoginPageView, RegisterPageView, ProfileDetailsView
urlpatterns = (
    path("login/", LoginPageView.as_view(), name="login_page"),
    path("register/", RegisterPageView.as_view(), name="register_page"),
    path("details/", ProfileDetailsView.as_view(), name="profile_details"),
)
