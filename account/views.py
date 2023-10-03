from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from basket.basket import NavBar_Basket_count
from .models import User, Customer
from .validators.validate import PasswordChecker
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Category
from django.db.models import Q

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
        customer = Customer.objects.filter(user=request.user)
        context = {
            "cart_count" : cart_count.calculate(),
            "categories" : categories,
            "customer" : customer,
        }
        return render(request, "base/profile.html", context=context)
    


class AddProfileView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "cart_count" : cart_count.calculate(),
            "categories" : categories,
        }
        return render(request, "base/addprofile.html", context=context)
    
    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        cities = request.POST.get('cities')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        profile = Customer.objects.create(user=request.user, first_name=first_name, last_name=last_name, gender=gender,
                                          country=country, phone=phonenumber, address=address, city=cities, state=state, pincode=pincode)
        profile.save()
        messages.success(request, "Your profile Saved Successfully.")
        return redirect('profile')
    

class EditProfileView(View):
        def get(self, request,pk=None):
            categories = Category.objects.prefetch_related('sub_categories').all()
            cart_count = NavBar_Basket_count(request=request)
            customer = Customer.objects.get(Q(user=request.user) & Q(id=pk))

            context = {
                "cart_count" : cart_count.calculate(),
                "categories" : categories,
                "customer" : customer,
            }
            return render(request, "base/editprofile.html", context=context)
        
        def post(self, request, pk):
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            gender = request.POST.get('gender')
            country = request.POST.get('country')
            phonenumber = request.POST.get('phonenumber')
            address = request.POST.get('address')
            cities = request.POST.get('cities')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')

            customer = Customer.objects.get(Q(user=request.user) & Q(id=pk))

            customer.first_name = first_name
            customer.last_name = last_name
            customer.gender = gender
            customer.country = country
            customer.phone = phonenumber
            customer.address = address
            customer.city = cities
            customer.state = state
            customer.pincode = pincode

            customer.save()
            messages.success(request, "Your profile Edited Successfully.")
            return redirect('profile')


class DeleteProfileView(View):
    pass


