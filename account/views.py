from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from BaseID.email import EmailSend_ResetPassword
from basket.basket import NavBar_Basket_count
from .models import User, Customer
from .validators.validate import PasswordChecker
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Category
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class registerViews(View):
    # Unit Test Passed
    def get(self, request):
        return render(request, "accounts/register.html")
    
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
        return render(request, "accounts/register.html")
    

class loginViews(View):
    # Unit Test Passed
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/accounts/profile/')
        return render(request, "accounts/login.html")
    
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
        
        return render(request, "accounts/login.html")
    

class SendEmailResetPasswordView(View):
    def get(self, request):
        return render(request, "accounts/forgotpassword.html")
    
    def post(self, request):
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            data={
                'subject' : 'For Password Reset',
            }
            email = EmailSend_ResetPassword(data=data, email=email, uid=uid, token=token)
            email.mail()


            messages.success(request, 'Email sended successfully, Please check your inbox or spam folder.')
        else:
            messages.success(request, "Email does't Exist.")                          

        return render(request,"accounts/forgotpassword.html")
    
class ResetPasswordView(View):
    def get(self, request, uid=None, token=None):
        return render(request, "accounts/resetpassword.html")

    def post(self, request, uid, token):
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        check = PasswordChecker(request=request, password=password1,
                                 confirmpassword=password2)
        if check.PasswordConfirmPasswordChecker():
            return HttpResponseRedirect(request.path_info)
        
        uid = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=uid)

        if not PasswordResetTokenGenerator().check_token(user, token):
            messages.info(request, 'Token is not valid or expired.')
        user.set_password(password1)
        user.save()
        messages.success(request, 'Password Reset Successfully.')
        return redirect('login')




    

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
        return render(request, "accounts/profile.html", context=context)
    
    def post(self, request):
        image_upload = request.FILES['image-upload']
        user = User.objects.get(email=request.user)
        user.avatar = image_upload
        user.save()
        messages.success(request, "Profile Picture added Successfully.")
        return redirect('profile')


class AddProfileView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.prefetch_related('sub_categories').all()
        cart_count = NavBar_Basket_count(request=request)
        context = {
            "cart_count" : cart_count.calculate(),
            "categories" : categories,
        }
        return render(request, "accounts/addprofile.html", context=context)
    
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
            return render(request, "accounts/editprofile.html", context=context)
        
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
    def get(self, request, pk):
        customer = Customer.objects.get(Q(user=request.user) & Q(id=pk))
        customer.delete()
        messages.success(request, "Profile information deleted successfully.")
        return redirect('profile')


