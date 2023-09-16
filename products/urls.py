from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsView.as_view(), name='products'),
    path("product-view/", views.ProductShowView.as_view(), name='product-view'),
    path("checkout/", views.checkouts, name='checkout'),
]