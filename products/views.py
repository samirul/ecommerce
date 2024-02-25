import pdb
import razorpay
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views import View
from django.conf import settings

from basket.basket import NavBar_Basket_count
from .models import Category, Product, Cart, Coupon, OrderPlaced
from account.models import Customer
from django.db.models import Q, Avg

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from basket.checkout import PriceCalculate, ShippingPriceCalculator
from basket.checkoutExtraItemsView import CheckoutsExtraTemplateItemViews




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
            "total_amount": total_price,
            "total_price": total_price,
            "price" : price,

        }

        coupons = Cart.objects.filter(user=request.user)
        for coupon in coupons:
            coupon.price = total_price
            coupon.save()
            if coupon.coupon:
                context["total_price"] = total_price - coupon.coupon.discount_price
                context["discounted_price"] = coupon.coupon.discount_price
                coupon.price = total_price - coupon.coupon.discount_price
                coupon.save()

        return render(request, "products/checkout.html", context=context)
    
    def post(self, request):
        coupon_code = request.POST.get('coupon-code')
        cart_items = Cart.objects.filter(user=request.user)
        find_coupon_code = Coupon.objects.filter(coupon_code__iexact=coupon_code)

        if not find_coupon_code.exists():
            messages.info(request, f"Coupon Code - {coupon_code} isn't valid.")

        coupon_applied = False

        for cart_item in cart_items:
            if cart_item.coupon:
                messages.info(request, f"Coupon Code - {cart_item.coupon.coupon_code} already applied.")
            elif find_coupon_code:
                cart_item.coupon = find_coupon_code[0]
                cart_item.save()
                messages.success(request, f"Coupon Code - {coupon_code} applied.")
                coupon_applied = True
                break

        if not coupon_applied and not find_coupon_code:
            messages.info(request, f"Coupon Code - {coupon_code} isn't valid.")

        return redirect('checkout')
    
class RemoveCartView(LoginRequiredMixin, View):

    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(user=request.user) & Q(product=product_id))
        cart_.delete()

        checkouts_extra_template_items = CheckoutsExtraTemplateItemViews(request=request)

        (shipping_amount,
        price,
        total_price,
        cart_count,
        checkout_product_titles,
        product_quantity_price) = checkouts_extra_template_items.cartExtraDataItems()

        data = {
            "Cart_update" : cart_count.calculate(),
            "shipping_amount" : shipping_amount,
            "checkout": checkout_product_titles,
            "product_quantity_price": product_quantity_price,
            "total_amount": total_price,
            "total_price": total_price,
            "price" : price,
        }

        total_discount_price, discounted_price  = checkouts_extra_template_items.CouponApply()
        if total_discount_price and discounted_price:
            data["total_price"] = total_discount_price
            data["discounted_price"] = discounted_price

        return JsonResponse(data)
    

class PlusQuantityView(LoginRequiredMixin, View):

    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        cart_.quantity += 1
        cart_.save()

        checkouts_extra_template_items = CheckoutsExtraTemplateItemViews(request=request)

        (shipping_amount,
        price,
        total_price,
        cart_count,
        checkout_product_titles,
        product_quantity_price) = checkouts_extra_template_items.cartExtraDataItems()

        data ={
            "quantity" : cart_.quantity,
            "shipping_amount" : shipping_amount,
            "price" : price,
            "total_amount": total_price,
            "total_price": total_price,
            "checkout": checkout_product_titles,
            "product_quantity_price": product_quantity_price,
            "cart_count" : cart_count.calculate(),
        }

        total_discount_price, discounted_price  = checkouts_extra_template_items.CouponApply()
        if total_discount_price and discounted_price:
            data["total_price"] = total_discount_price
            data["discounted_price"] = discounted_price

        return JsonResponse(data)


class MinusQuantityView(LoginRequiredMixin, View):

    def get(self, request):
        product_id = request.GET['product_id']
        cart_ = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        cart_.quantity -= 1
        cart_.save()

        checkouts_extra_template_items = CheckoutsExtraTemplateItemViews(request=request)

        (shipping_amount,
        price,
        total_price,
        cart_count,
        checkout_product_titles,
        product_quantity_price) = checkouts_extra_template_items.cartExtraDataItems()

        data ={
            "quantity" : cart_.quantity,
            "shipping_amount" : shipping_amount,
            "price" : price,
            "total_amount": total_price,
            "total_price": total_price,
            "checkout": checkout_product_titles,
            "product_quantity_price": product_quantity_price,
            "cart_count" : cart_count.calculate(),
        }

        total_discount_price, discounted_price  = checkouts_extra_template_items.CouponApply()
        if total_discount_price and discounted_price:
            data["total_price"] = total_discount_price
            data["discounted_price"] = discounted_price

        return JsonResponse(data)



class PaymentView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            cart = Cart.objects.filter(user=request.user).last()
            cart_price = int(cart.price * 100)
            customer_name = request.GET.get('customer_name')
            customer_phone = request.GET.get('customer_phone')
            customer_email = request.user.email
            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

            payment_data = {
                "amount" : cart_price,
                "currency": "INR",
                "payment_capture" : 1
            }

            order = client.order.create(data=payment_data)

            order_id = order['id']

            context = {
                'order_id': order_id,
                'amount': cart_price,
                'name': customer_name,
                'email': customer_email,
                'phone': customer_phone
            }
            return render(request, 'products/payment.html', context=context)
        except Exception:
            messages.info(request, "Something is wrong please check in the cart or add profile information.")
            return redirect('checkout')

           

class OrderedPageView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            cart = Cart.objects.filter(user=request.user)
            customer = Customer.objects.filter(user=request.user)
            razorpay_payment_id = request.GET.get('razorpay_payment_id')
            razorpay_order_id = request.GET.get('razorpay_order_id')
            if razorpay_payment_id and razorpay_order_id is not None:
                for items in cart:
                    for custom in customer:
                        OrderPlaced.objects.create(
                        user=request.user,
                        customer = custom,
                        product= items.product,
                        quantity= items.quantity,
                        is_payment_accepted = True,
                        payment_method='Online Payment')
                cart.delete()

            return HttpResponse("Payment Success")
        except Exception:
            return HttpResponse("Something is Wrong")


class OrderedPageFailedView(LoginRequiredMixin, View):
    def get(self, request):
        error_metadata_payment_id = request.GET.get('error_metadata_payment_id')
        error_metadata_order_id = request.GET.get('error_metadata_order_id')
        if error_metadata_payment_id and error_metadata_order_id is not None:
            return HttpResponse("Payment Failed, Please Try again")
        



class OrderedPageCODView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            cart = Cart.objects.filter(user=request.user)
            customer = Customer.objects.filter(user=request.user)

            if cart and customer:
                for items in cart:
                    for custom in customer:
                        OrderPlaced.objects.create(
                        user=request.user,
                        customer = custom,
                        product= items.product,
                        quantity= items.quantity,
                        is_payment_accepted = False,
                        payment_method='Cash on Delivery')
                cart.delete()
                return HttpResponse("Thank you for Ordering")
            else:
                messages.info(request, "Something is wrong please check in the cart or add profile information.")
                return redirect('checkout')
        except Exception:
             return HttpResponse("Something is Wrong")


