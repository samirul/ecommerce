import re
from django.shortcuts import  HttpResponseRedirect
from django.contrib import messages

# Passed by Pytest by returning True or False

class PasswordChecker:
    def __init__(self, request, password, confirmpassword):
        self.request = request
        self.password = password
        self.confirmpassword = confirmpassword

    def PasswordConfirmPasswordChecker(self):
        if self.password != self.confirmpassword:
            messages.info(self.request, "Password and Confirm Password Doesn't match.")
            return HttpResponseRedirect(self.request.path_info)
        return None

    def PasswordValidator(self, min_len):
        if len(self.password) < min_len:
            messages.info(self.request, "Password must be minimum 8 characters long.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[A-Z]', self.password):
            messages.info(self.request, "Password must contain at least one uppercase letter.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[a-z]', self.password):
            messages.info(self.request, "Password must contain at least one lowercase letter.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[0-9]', self.password):
            messages.info(self.request, "Password must contain at least one digit.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', self.password):
            messages.info(self.request, "Password must contain at least one special character.")
            return HttpResponseRedirect(self.request.path_info)
        
    
