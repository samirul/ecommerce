from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginView.as_view(), name='login'),
    path("register/", views.registerView.as_view(), name='register'),
    path("modal/", views.ModalView.as_view(), name='modal')

]