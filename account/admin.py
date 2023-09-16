from django.contrib import admin
from .models import User, Customer

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
      'id', 'user_name','email','is_verified','is_active','is_admin'
    ]


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [
        'id','user','first_name','last_name','phone','address','city','state'
    ]