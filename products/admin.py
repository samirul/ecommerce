from django.contrib import admin
from .models import *

@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=[
        "id","category_name","category_description"
    ]


@admin.register(Subcategories)
class SubcategoriesModelAdmin(admin.ModelAdmin):
    list_display=[
        "id","subcategory_name","categories"
    ]