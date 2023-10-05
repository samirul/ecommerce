import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .choices import GENDER_CHOICES, STATE_CHOICES, CITY_CHOICES, COUNTRY_CHOICES
from BaseID.models import baseIDModel
from django.templatetags.static import static

class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None, password2=None):

        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, user_name, password=None):

        user = self.create_user(
            email,
            password=password,
            user_name=user_name,
            
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
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='profiles', blank=True)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=150, null=True, blank=True)
    base_uid = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

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
    

class Customer(baseIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=200, choices=CITY_CHOICES)
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    pincode = models.IntegerField(default=0)



    