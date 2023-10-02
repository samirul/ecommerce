from typing import Any
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View

from basket.basket import NavBar_Basket_count
from .models import User
from .validators.validate import PasswordChecker
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Category

class registerViews(View):
    # Unit Test Passed
    def get(self, request):
        return render(request, "base/register.html")
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        check = PasswordChecker(request=request, password=password,
                                 confirmpassword=confirmpassword)
        
        if check.PasswordConfirmPasswordChecker():
            return HttpResponseRedirect(request.path_info)

        if check.PasswordValidator(min_len=8):
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(user_name=username).exists():
            messages.info(request, f"{username} - Username Already Taken, Please Choose Another Username.")
            return HttpResponseRedirect(request.path_info)    
            
        if User.objects.filter(email=email).exists():
            messages.info(request, f"{email} - Email Already Taken, Please Choose Another Email.")
            return HttpResponseRedirect(request.path_info)

        userobjects = User.objects.create(user_name=username,
                                          email=email)
        userobjects.set_password(password)
        userobjects.save()
        messages.success(request, "Registration Successful, Please Verify Your Email.")
        return render(request, "base/register.html")
    

class loginViews(View):
    # Unit Test Passed
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/accounts/profile/')
        return render(request, "base/login.html")
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        
        if not User.objects.filter(email=email).exists():
             messages.info(request, f"{email} - Email isn't Registered, Please Register Your Account First.")

        auth_user = authenticate(username=email, password=password)

        if auth_user is not None:
            login(request, auth_user)
            messages.success(request, f"Login Successful, Welcome Back - {email}")

            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            messages.info(request,"Invalid Email or Password, Please Check Your Credentials.")
            HttpResponseRedirect(request.path_info)
        
        return render(request, "base/login.html")
    

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "cart_count" : cart_count.calculate(),
            "categories" : categories,
        }
        return render(request, "base/profile.html", context=context)

