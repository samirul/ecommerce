from django.db import models
from BaseID.models import baseIDModel
from account.models import User
from .choices import STATUS_CHOICES


class Categories(baseIDModel):
    category_name = models.CharField(max_length=150)
    category_description = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class Subcategories(baseIDModel):
    subcategory_name = models.CharField(max_length=150)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name

class Products(baseIDModel):
    product_title = models.CharField(max_length=150)
    product_slug = models.SlugField(unique=True, null=True, blank=True)
    product_selling_price = models.FloatField()
    product_discounted_price = models.FloatField()
    product_description = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='product_imgs')
    brand = models.CharField(max_length=150)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategories = models.ForeignKey(Subcategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title
    

class Coupon(baseIDModel):
    coupon_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=0)
    minimum_amount = models.IntegerField(default=0)


class Cart(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class OrderPlaced(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date =models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.id)