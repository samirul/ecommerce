from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    # path("items/products/<slug>/", views.HomeView.as_view(), name='slughome'),
    path("contact-us/", views.ContactUsView.as_view(), name='contact-us'),
    path("about/", views.AboutView.as_view(), name='about'),
    path("services/", views.ServiceView.as_view(), name='services'),
    # path("<slugcategory>/", views.CategorySlugLink.as_view(), name="categorysluglink")


]