from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "base/index.html")



def contactUs(request):
    return render(request, "base/contact-us.html")



def about(request):
    return render(request, "base/about.html")


def service(request):
    return render(request, "base/services.html")

