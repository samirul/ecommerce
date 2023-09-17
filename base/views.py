from django.shortcuts import render, redirect
from django.views import View
from products.models import Categories
from .models import HomeSlider, HomeMiddleBanner

# class CategorySlugLink(View):
#     def get(self, request, slugcategory):
#         categories = Categories.objects.get(category_link=slugcategory)
#         context={
#             "categories_slug" : categories
#         }
#         return render(request, "base/index.html", context=context)



class HomeView(View):
    def get(self, request):
         categories = Categories.objects.prefetch_related('sub_categories').all()
         slider = HomeSlider.objects.all()
         homemiddlebanner = HomeMiddleBanner.objects.all()
         context = {
            "categories" : categories,
            "sliders" : slider,
            "homemiddlebanner" : homemiddlebanner
            }
         return render(request, "base/index.html", context=context)
    
    # def get(self, request, slug):
    #     categories_slug = Categories.objects.get(category_link=slug)
    #     context = {
    #         "categories_slug" : categories_slug,
    #         }
    #     return render(request, "base/index.html", context=context)
    

class ContactUsView(View):
    def get(self, request):
        categories = Categories.objects.prefetch_related('sub_categories').all()
        context = {
            "categories" : categories,
            }
        return render(request, "base/contact-us.html", context=context)

class AboutView(View):
    def get(self, request):
        categories = Categories.objects.prefetch_related('sub_categories').all()
        context = {
            "categories" : categories,
            }
        return render(request, "base/about.html", context=context)
    
class ServiceView(View):
    def get(self, request):
        categories = Categories.objects.prefetch_related('sub_categories').all()
        context = {
            "categories" : categories,
            }
        return render(request, "base/services.html", context=context)


