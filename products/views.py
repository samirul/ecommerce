from django.shortcuts import render
from django.views import View
from .models import Category, Subcategory, Product, Tag
from django.db.models import Q
import json

class ProductsView(View):
    def get(self, request, slug=None):
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        context = {
            "categories" : categories,
            
        }
        get_Category = request.GET.get('category_name')
        get_subcategory = request.GET.get('subcategory_name')
        context['get_category_name'] = get_Category
        context['get_subcategory'] = get_subcategory
        if get_Category is not None:
            category_items = Product.objects.filter(categories__category_name=get_Category)
            context["category_items"]=category_items

        if get_subcategory is not None:
            sub_category_items = Product.objects.filter(subcategories__subcategory_name=get_subcategory)
            context["sub_category_items"]=sub_category_items
    
        
        return render(request, "base/products.html", context=context)


class ProductShowView(View):
    def get(self, request, slug, pk):
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        products = Product.objects.filter(Q(slug=slug) & Q(id=pk))
        context = {
            "categories" : categories,
            "products" : products,
        }

        return render(request, "base/product-view.html", context=context)
    
    def post(self, request, slug, pk):
        rating = request.POST['selectedRating']
        print(rating)
        print(slug, pk)
        return render(request, "base/product-view.html")
    

def checkouts(request):
    return render(request, "base/checkout.html")