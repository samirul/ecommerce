from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("contact-us/", views.contactUs, name='contact-us'),
    path("about/", views.about, name='about'),
    path("services/", views.service, name='services'),


]