from django.contrib import admin
from .models import(
    HomeSlider, HomeMiddleBanner,
      ContactUS, ContactInfo, AboutInfo,
      AboutUs, AboutTestimonial, ServiceImages, ServiceBigImage, ServiceRowTexts, Services, Testimonial)

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





class AboutUsAdminModel(admin.StackedInline):
    model = AboutUs


class AboutInfoAdminModel(admin.ModelAdmin):
    list_display = [
        "id", "information","about_img",
        "created_by","updated_by",
    ]

    inlines = [AboutUsAdminModel]



class AboutTestimonialAdmin(admin.StackedInline):
    model = AboutTestimonial
    extra = 2
    max_num = 2
    


class TestimonialAdmin(admin.ModelAdmin):
    list_display=[
        "id", "testimonial_name", "created_by", "updated_by"
    ]

    inlines = [AboutTestimonialAdmin]


class ServiceImagesAdmin(admin.StackedInline):
    model = ServiceImages
    extra = 3
    max_num = 3

class ServiceBigImageAdmin(admin.StackedInline):
    model = ServiceBigImage
    extra = 1
    max_num = 1

class ServiceRowTextsAdmin(admin.StackedInline):
    model = ServiceRowTexts
    extra = 6
    max_num = 6

class ServicesAdmin(admin.ModelAdmin):
    list_display=[
        "id", "title", "description", "created_by", "updated_by"
    ]

    inlines = [ServiceBigImageAdmin, ServiceImagesAdmin, ServiceRowTextsAdmin]

  




admin.site.register(AboutInfo, AboutInfoAdminModel)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Services, ServicesAdmin)