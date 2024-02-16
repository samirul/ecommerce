from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=[
        "id","category_name","category_description"
    ]


@admin.register(Subcategory)
class SubcategoriesModelAdmin(admin.ModelAdmin):
    list_display=[
        "id","subcategory_name","categories"
    ]

@admin.register(Product)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display =[
        "id","product_title","product_selling_price",
        "product_discounted_price","brand",
        "categories","subcategories","tags"
    ]

@admin.register(Tag)
class TagsModelAdmin(admin.ModelAdmin):
    list_display =[
        "id","innerTag","homeTag"
    ]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =[
        "id","user","product","quantity"
    ]

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display =[
        "id","coupon_code", "is_expired"
    ]

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user", "customer", "product", "quantity", "is_payment_accepted","ordered_date"
    ]
    readonly_fields = [
        "id", "user", "customer", "product", "quantity", "is_payment_accepted"
    ]
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(ProductType)

# admin.site.register(OrderPlaced)


