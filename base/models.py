from django.db import models
from BaseID.models import baseIDModel
from .choices import H_TAG_CHOICES, DIV_CLASS_TAG_CHOICES

class HomeSlider(baseIDModel):
    title_1 = models.CharField(max_length=150)
    title_2 = models.CharField(max_length=150)
    title_3 = models.CharField(max_length=150)
    img_slide_code = models.IntegerField(null=True, blank=True)
    url_button_link = models.CharField(max_length=60, default='products')
    objects = models.Manager()

    def __str__(self):
        return f"{self.title_1} {self.title_2} {self.title_3}"
    
    class Meta:
        verbose_name_plural = "Home Slider"
    
class HomeMiddleBanner(baseIDModel):
    img_name = models.CharField(max_length=70)
    h_tag = models.IntegerField(default=0, choices=H_TAG_CHOICES)
    div_class_tag = models.CharField(max_length=150, choices=DIV_CLASS_TAG_CHOICES, default="wthree_banner_bottom_left_grid_pos")
    title_1 = models.CharField(max_length=150, null=True, blank=True)
    title_2 = models.CharField(max_length=150, null=True, blank=True)
    title_3 = models.CharField(max_length=150, null=True, blank=True)
    i_tag_title_4 = models.CharField(max_length=150, null=True, blank=True)
    objects = models.Manager()


    class Meta:
        verbose_name_plural = "Home Middle Banner"


class ContactUS(baseIDModel):
    name = models.CharField(max_length=150)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=2000)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} {self.email}"
    
    class Meta:
        verbose_name_plural = "Contact Us"
    

class ContactInfo(baseIDModel):
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    call_to_us = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.address}  {self.email}  {str(self.call_to_us)}"
    
    class Meta:
        verbose_name_plural = "Contact Info"




class AboutInfo(baseIDModel):
    information = models.TextField(max_length=2000)
    about_img = models.ImageField(upload_to="about")
    objects = models.Manager()
    
    def __str__(self):
        return "About Info"

    class Meta:
        verbose_name_plural = "About Info"




class AboutUs(baseIDModel):
    about_info = models.ForeignKey(AboutInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='about_us')
    list_info = models.CharField(max_length=255, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return "About Us"


    class Meta:
        verbose_name_plural = "About Us"


class Testimonial(baseIDModel):
    testimonial_name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return str(self.testimonial_name)

class AboutTestimonial(baseIDModel):
    tesimonial_name = models.ForeignKey(Testimonial, on_delete=models.CASCADE, null=True, blank=True, related_name="about_testimonial")
    testimonials_text = models.TextField(max_length=400)
    testimonial_Writter = models.CharField(max_length=150)
    testimonial_Writter_category = models.CharField(max_length=100, default="Customer")
    objects = models.Manager()

    def __str__(self):
        return "About Testimonials"


    class Meta:
        verbose_name_plural = "About Testimonial"


class Services(baseIDModel):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = "Services"

class ServiceImages(baseIDModel):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, 
    null=True, blank=True, related_name="service_images")
    services_imgs = models.ImageField(upload_to='services')
    objects = models.Manager()

    def __str__(self):
        return "Service Images"
    
    class Meta:
        verbose_name_plural = "Service Images"


class ServiceBigImage(baseIDModel):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, 
    null=True, blank=True, related_name="service_big_image")
    service_big_img = models.ImageField(upload_to='services')
    objects = models.Manager()

    def __str__(self):
        return "Service Big Image"
    
    class Meta:
        verbose_name_plural = "Service Big Image"

class ServiceRowTexts(baseIDModel):
    services = models.ForeignKey(Services, on_delete=models.CASCADE,
    null=True, blank=True, related_name="service_row_texts")
    service_txts_rows = models.CharField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return "Service Row Texts"
    
    class Meta:
        verbose_name_plural = "Service Row Texts"
