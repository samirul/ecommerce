from django.urls import path
from . import views

urlpatterns = [
    path("all-products/", views.AllProducts.as_view(), name='all-products'),
    path("products/<slug>/", views.ProductsView.as_view(), name='productslugcategory'),
    path("products/<slug>/", views.ProductsView.as_view(), name='productslugsubcategory'),
    path("product-view/<slug>/<str:pk>/", views.ProductShowView.as_view(), name='product-view'),
    path("add-to-cart/", views.ProductAddToCart.as_view(), name='add-to-cart'),
    path("checkout/", views.CheckoutsView.as_view(), name='checkout'),
    path("remove-cart-items/", views.RemoveCartView.as_view(), name='remove-cart-items'),
    path("plus-cart-items/", views.PlusQuantityView.as_view(), name='plus-cart-items'),
    path("minus-cart-items/", views.MinusQuantityView.as_view(), name='minus-cart-items'),
    path("payment/", views.PaymentView.as_view(), name='payment'),
    path("order-placed/", views.OrderedPageView.as_view(), name='order-placed'),
    path("payment-failed/", views.OrderedPageFailedView.as_view(), name='payment-failed'),
    
]