from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .choices import GENDER_CHOICES, STATE_CHOICES, CITY_CHOICES, COUNTRY_CHOICES

class UserManager(BaseUserManager):
    def create_user(self, email, customer_user_name, customer_first_name, customer_last_name, password=None, password2=None):

        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            customer_user_name=customer_user_name,
            customer_first_name=customer_first_name,
            customer_last_name=customer_last_name
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, customer_user_name, customer_first_name, customer_last_name, password=None):

        user = self.create_user(
            email,
            password=password,
            customer_user_name=customer_user_name,
            customer_first_name=customer_first_name,
            customer_last_name=customer_last_name
            
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user
    



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    customer_user_name = models.CharField(max_length=150)
    customer_first_name = models.CharField(max_length=200)
    customer_last_name = models.CharField(max_length=200)
    customer_avatar = models.ImageField(upload_to='profiles', blank=True)
    customer_gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=200, choices=CITY_CHOICES)
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    pincode = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    activation_key = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['customer_user_name',
                       'customer_first_name',
                       'customer_last_name']

    def get_all_permissions(user=None):
        if user.is_admin:
            return set()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    