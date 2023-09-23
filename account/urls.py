from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("register/", views.registerViews.as_view(), name='register'),
    path("login/", views.loginViews.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
    path("profile/", views.ProfileView.as_view(), name='profile')

]