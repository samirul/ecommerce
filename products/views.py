from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View

from basket.basket import NavBar_Basket_count
from .models import Category, Product, Cart
from account.models import Customer
from django.db.models import Q, Avg

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import pdb

from basket.checkout import PriceCalculate, ShippingPriceCalculator



class AllProducts(View):
    def get(self, request):
        #pdb.set_trace()
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context={
            "categories" : categories,
            "cart_count" : cart_count.calculate(),
        }

        category_name = request.GET.get('category_name')
        context['category_name'] = category_name

        return render(request, "products/all-products.html", context=context)



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
    
        
        return render(request, "products/products.html", context=context)


class ProductShowView(View):
    def get(self, request, slug, pk):
        categories = Category.objects.prefetch_related('sub_categories','product_categories').all()
        products = Product.objects.filter(Q(slug=slug) & Q(id=pk))
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "categories" : categories,
            "products" : products,
            "cart_count" : cart_count.calculate(),
        }

        return render(request, "products/product-view.html", context=context)
    
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
        return render(request, "products/product-view.html")


class ProductAddToCart(LoginRequiredMixin, View):
    def get(self, request):
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        check_Cart_items = Cart.objects.filter(Q(user=request.user) & Q(product=product_id))
        if not check_Cart_items.exists():
            Cart(user=request.user, product=product).save()
            messages.success(request, f"{product.product_title} Added in cart.")
        else:
            for qty in check_Cart_items:
                if qty.quantity == 12:
                    messages.info(request, f"{product.product_title} Max Quantity reached, You Can't Order More Than - {qty.quantity} at a Time or Not Avaliable.")
                else:    
                    qty.quantity += 1
                    qty.save()
                    messages.success(request, f"{product.product_title} Added to cart, Quantity {qty.quantity}")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CheckoutsView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        checkout = Cart.objects.filter(user=request.user)
        customer = Customer.objects.filter(user=request.user)
        cart_product_items = [items for items in Cart.objects.all() if items.user == request.user]
        shipping_amount_calculator = ShippingPriceCalculator(request=request, cart_product_items=cart_product_items, shipping_amount=50)
        shipping_amount = shipping_amount_calculator.shipping_calculate()
        price_calculate = PriceCalculate(cart_product_items=cart_product_items, shipping_amount=shipping_amount)
        price, total_price = price_calculate.calculate()

        context ={
            "cart_count" : cart_count.calculate(),
            "checkout" : checkout,
            "categories" : categories,
            "customer" : customer,
            "shipping_amount" : shipping_amount,
            "total_price": total_price,
            "price" : price,

        }
        return render(request, "products/checkout.html", context=context)
    
class RemoveCartView(LoginRequiredMixin, View):
    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(user=request.user) & Q(product=product_id))
        cart_.delete()
        cart_count = NavBar_Basket_count(request=request)
        cart_product_items = [items for items in Cart.objects.all() if items.user == request.user]
        shipping_amount_calculator = ShippingPriceCalculator(request=request, cart_product_items=cart_product_items, shipping_amount=50)
        shipping_amount = shipping_amount_calculator.shipping_calculate()
        price_calculate = PriceCalculate(cart_product_items=cart_product_items, shipping_amount=shipping_amount)
        price, total_price = price_calculate.calculate()
        data = {
            "Cart_update" : cart_count.calculate(),
            "shipping_amount" : shipping_amount,
            "checkout": [],
            "product_quantity_price": [],
            "total_price" : total_price,
            "price" : price,
        }
        checkouts = Cart.objects.filter(user=request.user)
        for check in checkouts:
            data["checkout"].append(check.product.product_title)
            data["product_quantity_price"].append(check.product_quantity_price)
        return JsonResponse(data)
    

class PlusQuantityView(LoginRequiredMixin, View):
    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        cart_.quantity += 1
        cart_.save()
        cart_product_items = [items for items in Cart.objects.all() if items.user == request.user]
        shipping_amount_calculator = ShippingPriceCalculator(request=request, cart_product_items=cart_product_items, shipping_amount=50)
        shipping_amount = shipping_amount_calculator.shipping_calculate()
        price_calculate = PriceCalculate(cart_product_items=cart_product_items, shipping_amount=shipping_amount)
        price, total_price = price_calculate.calculate()
        cart_count = NavBar_Basket_count(request=request)
        
        data ={
            "quantity" : cart_.quantity,
            "shipping_amount" : shipping_amount,
            "price" : price,
            "total_price" : total_price,
            "checkout": [],
            "product_quantity_price": [],
            "cart_count" : cart_count.calculate(),
        }

        checkouts = Cart.objects.filter(user=request.user)
        for check in checkouts:
            data["checkout"].append(check.product.product_title)
            data["product_quantity_price"].append(check.product_quantity_price)
        return JsonResponse(data)


class MinusQuantityView(LoginRequiredMixin, View):

    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        cart_.quantity -= 1
        cart_.save()
        cart_product_items = [items for items in Cart.objects.all() if items.user == request.user]
        shipping_amount_calculator = ShippingPriceCalculator(request=request, cart_product_items=cart_product_items, shipping_amount=50)
        shipping_amount = shipping_amount_calculator.shipping_calculate()
        price_calculate = PriceCalculate(cart_product_items=cart_product_items, shipping_amount=shipping_amount)
        price, total_price = price_calculate.calculate()
        cart_count = NavBar_Basket_count(request=request)
        
        data ={
            "quantity" : cart_.quantity,
            "shipping_amount" : shipping_amount,
            "price" : price,
            "total_price" : total_price,
            "checkout": [],
            "product_quantity_price": [],
            "cart_count" : cart_count.calculate(),
        }

        checkouts = Cart.objects.filter(user=request.user)
        for check in checkouts:
            data["checkout"].append(check.product.product_title)
            data["product_quantity_price"].append(check.product_quantity_price)
        return JsonResponse(data)



