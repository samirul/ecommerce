from django.shortcuts import render
from django.views import View
from .models import Categories, Subcategories
# Create your views here.


class ProductsView(View):
    def get(self, request):
        categories = Categories.objects.prefetch_related('sub_categories').all()
        context = {
            "categories" : categories,
        }
        return render(request, "base/products.html", context=context)


class ProductShowView(View):
    def get(self, request):
        categories = Categories.objects.prefetch_related('sub_categories').all()
        context = {
            "categories" : categories,
        }
        return render(request, "base/product-view.html", context=context)

def checkouts(request):
    return render(request, "base/checkout.html")