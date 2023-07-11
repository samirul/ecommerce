from django.shortcuts import render

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