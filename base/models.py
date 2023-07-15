from django.db import models
from BaseID.models import baseIDModel
# Create your models here.

class Categories(baseIDModel):
    category_name = models.CharField(max_length=150, unique=True)

class Subcategories(baseIDModel):
    subcategory_name = models.CharField(max_length=150, unique=True)
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Products(baseIDModel):
    product_name = models.CharField(max_length=150, unique=True)
    product_description = models.CharField(max_length=255)
    product_price = models.IntegerField(default=0)