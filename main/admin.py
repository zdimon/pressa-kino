from django.contrib import admin
from main.models import *
from image_cropping import ImageCroppingMixin


# Register your models here.
class FestivalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Festival, FestivalAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ("title","in_menu" )

admin.site.register(Page, PageAdmin)


class FilmAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("thumb","name","festival" )

admin.site.register(Film, FilmAdmin)


class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("thumb","name")

admin.site.register(Blog, BlogAdmin)
