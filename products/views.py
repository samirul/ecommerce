from django.shortcuts import render
from django.views import View
from .models import Category, Subcategory, Product, Tag
from django.db.models import Q

class ProductsView(View):
    def get(self, request, slug=None):
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        tags = Tag.objects.all()
        context = {
            "categories" : categories,
            "tags" : tags,
        }
        get_Category = request.GET.get('category_name')
        get_subcategory = request.GET.get('subcategory_name')
        tags_product = request.GET.get('tag-name')
        print(tags_product)
        context['get_category_name'] = get_Category
        context['get_subcategory'] = get_subcategory
        if get_Category is not None:
            category_items = Product.objects.filter(Q(categories__category_name=get_Category) & Q(tags__innerTag='Foods'))
            context["category_items"]=category_items

        if get_subcategory is not None:
            sub_category_items = Product.objects.filter(Q(subcategories__subcategory_name=get_Category) & Q(tags__innerTag=tags_product))
            context["sub_category_items"]=sub_category_items
    
        
        return render(request, "base/products.html", context=context)


class ProductShowView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        context = {
            "categories" : categories,
        }
        return render(request, "base/product-view.html", context=context)

def checkouts(request):
    return render(request, "base/checkout.html")