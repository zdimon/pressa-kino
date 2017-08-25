from django.contrib import admin
from main.models import *
from image_cropping import ImageCroppingMixin


# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ("name","text", "is_published", "film" )
    list_editable = ('is_published',)

admin.site.register(Message, MessageAdmin)

class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ("title","is_in_catalog" )

admin.site.register(Festival, FestivalAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ("title","in_menu" )

admin.site.register(Page, PageAdmin)

class VideoInline(admin.TabularInline):
    list_display = ("code","video" )
    model = Videos



class FilmAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("thumb","name","festival", "catalog", 'votes' )
    inlines = [ VideoInline, ]

admin.site.register(Film, FilmAdmin)


class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("thumb","name")

admin.site.register(Blog, BlogAdmin)


class CatalogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Catalog, CatalogAdmin)
