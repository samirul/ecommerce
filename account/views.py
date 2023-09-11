from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, "base/register.html")


def login(request):
    return render(request, "base/login.html")