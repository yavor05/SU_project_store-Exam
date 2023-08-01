from django.urls import path
from .views import LoginPageView, UserRegisterView, ProfileDetailsView, LogoutPageView
urlpatterns = (
    path("login/", LoginPageView.as_view(), name="login_page"),
    path("register/", UserRegisterView.as_view(), name="register_page"),
    path("details/<int:pk>/", ProfileDetailsView.as_view(), name="profile_details"),
    path("logout/", LogoutPageView.as_view(), name="logout_page"),
)
