from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .models import User


# Create your views here.

# def register(request):
#     return render(request, "base/register.html")


def login(request):
    return render(request, "base/login.html")


class registerView(View):
    def get(self, request):
        return render(request, "base/register.html")
    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password != confirmpassword:
            print("Password and Confirm Password Doesn't match.")
            return HttpResponseRedirect(request.path_info)

        if len(password) < 8:
            print("Password should be minimum 8 length.")
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(email=email).exists():
            print("Email Already Exist.")
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(customer_user_name=username).exists():
            print("Username Already Exist.")
            return HttpResponseRedirect(request.path_info)

        userobjects = User.objects.create(customer_user_name=username,
                                          customer_first_name=firstname,
                                          customer_last_name=lastname,
                                          email=email)
        userobjects.set_password(password)
        userobjects.save()
        print("Registration Successful.")
        return render(request, "base/register.html")