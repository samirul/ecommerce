from django.contrib import admin
from .models import HomeSlider, HomeMiddleBanner

@admin.register(HomeSlider)
class SliderAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "title_1","title_2","title_3",
        "img_slide_code","url_button_link",
    ]


@admin.register(HomeMiddleBanner)
class SliderAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "img_name","h_tag","div_class_tag",
        "title_1","title_2","title_3",
        "i_tag_title_4",
    ]
