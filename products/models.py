from django.db import models
from BaseID.models import baseIDModel
from account.models import User
from .choices import STATUS_CHOICES
from django.utils.text import slugify


class Category(baseIDModel):
    category_name = models.CharField(max_length=150)
    category_description = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

class Subcategory(baseIDModel):
    subcategory_name = models.CharField(max_length=150)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.subcategory_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subcategory_name)
        super(Subcategory, self).save(*args, **kwargs)


class Tag(baseIDModel):
    innerTag = models.CharField(max_length=150, null=True, blank=True)
    homeTag = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.innerTag}, {self.homeTag}"

class Product(baseIDModel):
    product_title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)
    product_selling_price = models.FloatField()
    product_discounted_price = models.FloatField()
    product_rating = models.IntegerField(default=0)
    product_description = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='product_imgs')
    brand = models.CharField(max_length=150)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_categories')
    subcategories = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.product_title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_title)
        super(Product, self).save(*args, **kwargs)


class Coupon(baseIDModel):
    coupon_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=0)
    minimum_amount = models.IntegerField(default=0)


class Cart(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        self.quantity = max(self.quantity, 1)
        super().save(*args, **kwargs)

    @property
    def product_quantity_price(self):
        return self.quantity * self.product.product_discounted_price
    


class OrderPlaced(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date =models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.id)