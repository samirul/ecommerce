import re
from django.shortcuts import  HttpResponseRedirect

class PasswordChecker:
    def __init__(self, request, password, confirmpassword):
        self.request = request
        self.password = password
        self.confirmpassword = confirmpassword

    def PasswordConfirmPasswordChecker(self):
        if self.password != self.confirmpassword:
            print("Password and Confirm Password Doesn't match.")
            return HttpResponseRedirect(self.request.path_info)

    def PasswordValidator(self, min_len):
        if len(self.password) < min_len:
            print("Password must be minimum 8 characters long.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[A-Z]', self.password):
            print("Password must contain at least one uppercase letter.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[a-z]', self.password):
            print("Password must contain at least one lowercase letter.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[0-9]', self.password):
            print("Password must contain at least one digit.")
            return HttpResponseRedirect(self.request.path_info)
        
        if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', self.password):
            print("Password must contain at least one special character.")
            return HttpResponseRedirect(self.request.path_info)
        
    
