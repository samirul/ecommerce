from django.urls import path
from . import views

urlpatterns = [
    path("products/<slug>/", views.ProductsView.as_view(), name='productslugcategory'),
    path("products/<slug>/", views.ProductsView.as_view(), name='productslugsubcategory'),
    path("product-view/<slug>/<str:pk>/", views.ProductShowView.as_view(), name='product-view'),
    path("add-to-cart/", views.ProductAddToCart.as_view(), name='add-to-cart'),
    path("checkout/", views.CheckoutsView.as_view(), name='checkout'),
    path("remove-cart-items/", views.RemoveCartView.as_view(), name='remove-cart-items')
]