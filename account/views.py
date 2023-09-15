from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from .models import User
from .validators.validate import PasswordChecker
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


class registerView(View):
    # Test Passed
    def get(self, request):
        return render(request, "base/register.html")
    
    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        check = PasswordChecker(request=request, password=password,
                                 confirmpassword=confirmpassword)
        
        if check.PasswordConfirmPasswordChecker():
            return HttpResponseRedirect(request.path_info)

        if check.PasswordValidator(min_len=8):
            return HttpResponseRedirect(request.path_info)

        if User.objects.filter(customer_user_name=username).exists():
            messages.info(request, f"{username} - Username Already Taken, Please Choose Another Username.")
            return HttpResponseRedirect(request.path_info)    
            
        if User.objects.filter(email=email).exists():
            messages.info(request, f"{email} - Email Already Taken, Please Choose Another Email.")
            return HttpResponseRedirect(request.path_info)

        userobjects = User.objects.create(customer_user_name=username,
                                          customer_first_name=firstname,
                                          customer_last_name=lastname,
                                          email=email)
        userobjects.set_password(password)
        userobjects.save()
        messages.success(request, "Registration Successful, Please Verify Your Email.")
        return render(request, "base/register.html")
    

class loginView(View):
    def get(self, request):
        return render(request, "base/login.html")
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
             messages.info(request, f"{email} - Email isn't Registered, Please Register Your Account First.")

        auth_user = authenticate(username=email, password=password)

        if auth_user:
            login(request, auth_user)
            messages.success(request, f"Login Successful, Welcome Back - {email}")
            return redirect('/')
        else:
            messages.info(request,"Invalid Email or Password, Please Check Your Credentials.")
            HttpResponseRedirect(request.path_info)
        
        return render(request, "base/login.html")
    




class ModalView(View):
    def get(request):
        return render(request, 'base/modal.html')