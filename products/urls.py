from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products, name='products'),
    path("product-view/", views.productview, name='product-view'),
    path("checkout/", views.checkouts, name='checkout'),
]