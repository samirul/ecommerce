from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request, "base/products.html")


def productview(request):
    return render(request, "base/product-view.html")



def checkouts(request):
    return render(request, "base/checkout.html")