from django.db import models
from BaseID.models import baseIDModel
from account.models import User

# Create your models here.

CATEGORIES_CHOICES =()

SUBCATEGORIES_CHOICES =()


STATUS_CHOICES =()


class Categories(baseIDModel):
    category_name = models.CharField(choices=CATEGORIES_CHOICES, max_length=150)
    category_description = models.CharField(max_length=150)

class Subcategories(baseIDModel):
    subcategory_name = models.CharField(choices=SUBCATEGORIES_CHOICES, max_length=150)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Products(baseIDModel):
    product_title = models.CharField(max_length=150)
    product_selling_price = models.FloatField()
    product_discounted_price = models.FloatField()
    product_description = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='product_imgs')
    brand = models.CharField(max_length=150)
    categories = models.ManyToManyField(Categories, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(Subcategories, on_delete=models.CASCADE)


class Cart(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class OrderPlaced(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date =models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')