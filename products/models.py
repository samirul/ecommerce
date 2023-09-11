from django.db import models
from BaseID.models import baseIDModel

# Create your models here.

class Categories(baseIDModel):
    category_name = models.CharField(max_length=150)

class Subcategories(baseIDModel):
    subcategory_name = models.CharField(max_length=150)
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Products(baseIDModel):
    product_title = models.CharField(max_length=150)
    product_selling_price = models.FloatField()
    product_discounted_price = models.FloatField()
    product_description = models.CharField(max_length=255)
    product_price = models.IntegerField(default=0)