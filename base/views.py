from django.shortcuts import render, redirect
from django.views import View
from basket.basket import NavBar_Basket_count
from products.models import Category, Product
from .models import *
from django.contrib import messages


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
        contact_info = ContactInfo.objects.all()
        context = {
            "categories" : categories,
            "cart_count" : cart_count.calculate(),
            "contact_info" : contact_info
            }
        return render(request, "base/contact-us.html", context=context)
    def post(self, request): 
        try:
            name = request.POST.get("Name")
            telephone = request.POST.get("Telephone")
            email = request.POST.get("Email")
            subject = request.POST.get("Subject")
            message = request.POST.get("Message")
            contact = ContactUS.objects.create(name=name, telephone=telephone, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, "Your Request Has Been Received, Please Allow Us To Get Back To You Within 2 Days.")
            return redirect('contact-us')
        except Exception:
            messages.info(request, "Something Is Wrong Please Try Again.")
            return redirect('contact-us')
    
class AboutView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        about_infos =AboutInfo.objects.all()
        context = {
            "categories" : categories,
            "cart_count" : cart_count.calculate(),
            "about_infos" : about_infos
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


