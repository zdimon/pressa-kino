# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from image_cropping import ImageRatioField
from django.core.urlresolvers import reverse


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=250,verbose_name=_(u'заголовок'))
    image  = models.ImageField(upload_to='page', verbose_name=u'Изображение', blank=True, null=True)
    video  = models.FileField(upload_to='video', verbose_name=u'Видео', blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    alias = models.CharField(max_length=50,verbose_name=_(u'псевдоним'),help_text="не менять!", db_index=True)
    in_menu = models.BooleanField(verbose_name=_(u'в верхнем меню?'),default=False)
    code = models.TextField(verbose_name=_(u'код для всавки'), blank=True, null=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = _(u'страница')
        verbose_name_plural = _(u'страницы')


class Festival(models.Model):
    title = models.CharField(max_length=250,verbose_name=_(u'заголовок'))
    image  = models.ImageField(upload_to='festivals', verbose_name=u'Изображение', blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    alias = models.CharField(max_length=50,verbose_name=_(u'псевдоним'), db_index=True)
    
    def get_absolute_url(self):
        return reverse('festival_detail', args=[self.alias])
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = _(u'кинофестиваль')
        verbose_name_plural = _(u'фестиваль')


class Film(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    name = models.CharField(max_length=250,verbose_name=_(u'заголовок'))
    shorttext = models.TextField(verbose_name=_(u'краткое описание'), blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    image  = models.ImageField(upload_to='film', verbose_name=u'Изображение', blank=True, null=True)
    cropping = ImageRatioField('image', '255x145')
    def __unicode__(self):
        return self.name

    @property
    def thumb_url(self):
        if self.image:
            im = get_thumbnail(self.image, '255x145', crop='top')
            return im.url
        else:
            return None

    @property
    def thumb(self):
        if self.image:
            return mark_safe('<img src="%s" />' % self.thumb_url)
        else:
            return None
    class Meta:
        verbose_name = _(u'фильм')
        verbose_name_plural = _(u'фильмы')

class Videos(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    code = models.TextField(verbose_name=_(u'код для вставки'), blank=True, null=True)
    video  = models.FileField(upload_to='video', verbose_name=u'Видео', blank=True, null=True)     



class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'заголовок'))
    shorttext = models.TextField(verbose_name=_(u'краткое описание'), blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    image  = models.ImageField(upload_to='blog', verbose_name=u'Изображение', blank=True, null=True)
    cropping = ImageRatioField('image', '180x180')
    def __unicode__(self):
        return self.name
    @property
    def thumb_url(self):
        if self.image:
            im = get_thumbnail(self.image, '180x180', crop='top')
            return im.url
        else:
            return None
    @property
    def thumb(self):
        if self.image:
            return mark_safe('<img src="%s" />' % self.thumb_url)
        else:
            return None
    class Meta:
        verbose_name = _(u'блог')
        verbose_name_plural = _(u'блог')
