from django.contrib import admin
from .models import HomeSlider, HomeMiddleBanner, ContactUS, ContactInfo

@admin.register(HomeSlider)
class HomeSliderAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "title_1","title_2","title_3",
        "img_slide_code","url_button_link",
    ]


@admin.register(HomeMiddleBanner)
class HomeMiddleBannerAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "img_name","h_tag","div_class_tag",
        "title_1","title_2","title_3",
        "i_tag_title_4",
    ]


@admin.register(ContactUS)
class ContactUsAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "name","telephone","email",
        "subject", "created_by","updated_by",
    ]

@admin.register(ContactInfo)
class ContactInfoAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "address","email","call_to_us",
        "created_by","updated_by",
    ]
