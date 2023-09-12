from django.contrib import admin
from .models import User

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
      'id','customer_first_name', 'customer_last_name',
      'customer_gender','country','phone','address',
      'is_verified','is_active','is_admin'
    ]