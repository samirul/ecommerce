from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views import View

from basket.basket import NavBar_Basket_count
from .models import Category, Subcategory, Product, Tag, Cart
from django.db.models import Q, Avg

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class ProductsView(View):
    def get(self, request, slug=None):
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "categories" : categories,
            "cart_count" : cart_count.calculate(),
            
            
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
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "categories" : categories,
            "products" : products,
            "cart_count" : cart_count.calculate()
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


class ProductAddToCart(LoginRequiredMixin, View):
    def get(self, request):
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        check_Cart_items = Cart.objects.filter(Q(user=request.user) & Q(product=product_id))
        if not check_Cart_items.exists():
            Cart(user=request.user, product=product).save()
            messages.success(request, f"{product.product_title} Added in cart.")
        else:
            messages.info(request, f"{product.product_title} Already in cart.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CheckoutsView(LoginRequiredMixin, View):
    def get(self, request):
        cart_count = NavBar_Basket_count(request=request)
        checkout = Cart.objects.filter(user=request.user)
        context ={
            "cart_count" : cart_count.calculate(),
            "checkout" : checkout
        }
        return render(request, "base/checkout.html", context=context)
    
class RemoveCartView(LoginRequiredMixin, View):
    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(user=request.user) & Q(product=product_id))
        cart_.delete()

        cart_count = NavBar_Basket_count(request=request)


        data = {
            "product_image" : cart_.product.product_image.url,
            "product_quantity" : cart_.quantity,
            "product_name" : cart_.product.product_title,
            "product_price" : cart_.product.product_discounted_price,
            "Cart_update" : cart_count.calculate()
        }

        return JsonResponse(data)
    


    

