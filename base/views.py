from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "base/index.html")


def register(request):
    return render(request, "base/register.html")


def login(request):
    return render(request, "base/login.html")


def todayspecialoffer(request):
    return render(request, "base/products.html")