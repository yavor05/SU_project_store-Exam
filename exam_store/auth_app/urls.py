from django.urls import path
from .views import login_view, register_view, ProfileDetailsView, logout_user, UserEditView

urlpatterns = (
    path("login/", login_view, name="login_page"),
    path("register/", register_view, name="register_page"),
    path("details/<int:pk>/", ProfileDetailsView.as_view(), name="profile_details"),
    path("logout/", logout_user, name="logout_page"),
    path("edit/", UserEditView.as_view(), name="user_edit_page"),
)
