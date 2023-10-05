from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("register/", views.registerViews.as_view(), name='register'),
    path("login/", views.loginViews.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("add-profile/", views.AddProfileView.as_view(), name='add-profile'),
    path("edit-profile/<str:pk>/", views.EditProfileView.as_view(), name='edit-profile'),
    path("delete-profile/<str:pk>/", views.DeleteProfileView.as_view(), name='delete-profile'),
    path("reset-profile-password-send-email/", views.SendEmailResetPasswordView.as_view(), name='reset-profile-password-send-email'),
    path("reset-profile-password/<uid>/<token>/", views.ResetPasswordView.as_view(), name='reset-profile-password-send-email'),

]