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

class GSTFivePercentAdmin(admin.StackedInline):
    model = GSTFivePercent
    extra = 1
    max_num = 12

class GSTTwelvePercentAdmin(admin.StackedInline):
    model = GSTTwelvePercent
    extra = 1
    max_num = 12

class GSTEighteenPercentAdmin(admin.StackedInline):
    model = GSTEighteenPercent
    extra = 1
    max_num = 12


class GSTZeroPercentAdmin(admin.StackedInline):
    model = GSTZeroPercent
    extra = 1
    max_num = 12
    


class GSTAdmin(admin.ModelAdmin):
    list_display = [
        "id", "name"
    ]

    inlines = [GSTZeroPercentAdmin, GSTFivePercentAdmin, GSTTwelvePercentAdmin, GSTEighteenPercentAdmin]



admin.site.register(ProductType)
admin.site.register(GST, GSTAdmin)

