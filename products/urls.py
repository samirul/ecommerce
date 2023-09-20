from django.urls import path
from . import views

urlpatterns = [
    path("products/<slug>/", views.ProductsView.as_view(), name='productslugcategory'),
    path("products/<slug>/", views.ProductsView.as_view(), name='productslugsubcategory'),
    path("product-view/<slug>/<str:pk>/", views.ProductShowView.as_view(), name='product-view'),
    path("checkout/", views.checkouts, name='checkout'),
]