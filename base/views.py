from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "base/index.html")


def register(request):
    return render(request, "base/register.html")


def login(request):
    return render(request, "base/login.html")


def products(request):
    return render(request, "base/products.html")



def contactUs(request):
    return render(request, "base/contact-us.html")



def about(request):
    return render(request, "base/about.html")


def service(request):
    return render(request, "base/services.html")


def productview(request):
    return render(request, "base/product-view.html")


def checkouts(request):
    return render(request, "base/checkout.html")