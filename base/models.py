from django.db import models
from BaseID.models import baseIDModel
from .choices import H_TAG_CHOICES, DIV_CLASS_TAG_CHOICES

class HomeSlider(baseIDModel):
    title_1 = models.CharField(max_length=150)
    title_2 = models.CharField(max_length=150)
    title_3 = models.CharField(max_length=150)
    img_slide_code = models.IntegerField(null=True, blank=True)
    url_button_link = models.CharField(max_length=60, default='products')

    def __str__(self):
        return self.title_1 + self.title_2 + self.title_3
    
class HomeMiddleBanner(baseIDModel):
    img_name = models.CharField(max_length=70)
    h_tag = models.IntegerField(default=0, choices=H_TAG_CHOICES)
    div_class_tag = models.CharField(max_length=150, choices=DIV_CLASS_TAG_CHOICES, default="wthree_banner_bottom_left_grid_pos")
    title_1 = models.CharField(max_length=150, null=True, blank=True)
    title_2 = models.CharField(max_length=150, null=True, blank=True)
    title_3 = models.CharField(max_length=150, null=True, blank=True)
    i_tag_title_4 = models.CharField(max_length=150, null=True, blank=True)




