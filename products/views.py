from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Subcategory, Product, Tag, Cart
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    
    def post(self, request, slug=None, pk=None):
        rating = request.POST.get('selectedRating')
        print(f"rating is : {rating}")
        products = Product.objects.filter(Q(slug=slug) & Q(id=pk))
        for product in products:
            product.product_rating = rating
            product.save()

        products = Product.objects.filter(Q(slug=slug) & Q(id=pk))
        for product in products:
            product.product_rating = Product.objects.filter(Q(slug=slug) & Q(id=pk)).aggregate(Avg('product_rating'))['product_rating__avg']
            product.save()
        return render(request, "base/product-view.html")

@method_decorator(login_required, name='dispatch')
class ProductAddToCart(View):
    def get(self, request):
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        check_Cart_items = Cart.objects.filter(Q(user=request.user) & Q(product=product_id))
        if not check_Cart_items.exists():
            Cart(user=request.user, product=product).save()
        print( f"id is: {product_id}")
        return redirect('checkout')


class CheckoutsView(View):
    def get(self, request):
        return render(request, "base/checkout.html")