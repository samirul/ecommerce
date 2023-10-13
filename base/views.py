from django.shortcuts import render, redirect
from django.views import View
from basket.basket import NavBar_Basket_count
from products.models import Category, Product
from .models import HomeSlider, HomeMiddleBanner

class HomeView(View):
    def get(self, request):
         categories = Category.objects.prefetch_related('sub_categories').all()
         slider = HomeSlider.objects.all()
         homemiddlebanner = HomeMiddleBanner.objects.all()
         cart_count = NavBar_Basket_count(request=request)
         hot_offers = Product.objects.filter(tags__homeTag__exact="Hot Offers")
         context = {
            "categories" : categories,
            "sliders" : slider,
            "homemiddlebanner" : homemiddlebanner,
            "cart_count" : cart_count.calculate(),
            "hot_offers" : hot_offers
            }
         return render(request, "base/index.html", context=context)

class ContactUsView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "categories" : categories,
            "cart_count" : cart_count.calculate()
            }
        return render(request, "base/contact-us.html", context=context)

class AboutView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "categories" : categories,
            "cart_count" : cart_count.calculate()
            }
        return render(request, "base/about.html", context=context)
    
class ServiceView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "categories" : categories,
            "cart_count" : cart_count.calculate()
            }
        return render(request, "base/services.html", context=context)


