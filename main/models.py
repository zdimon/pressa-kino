# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from image_cropping import ImageRatioField
from django.core.urlresolvers import reverse
import pytils

# Create your models here.

class Vote(models.Model):
    obj = models.IntegerField(verbose_name=_(u'объект'), default=0)
    cnt = models.IntegerField(verbose_name=_(u'кол-во голосов'), default=0)
    score = models.IntegerField(verbose_name=_(u'балы'), default=0)

class Page(models.Model):
    title = models.CharField(max_length=250,verbose_name=_(u'заголовок'))
    image  = models.ImageField(upload_to='page', verbose_name=u'Изображение', blank=True, null=True)
    video  = models.FileField(upload_to='video', verbose_name=u'Видео', blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    alias = models.CharField(max_length=50,verbose_name=_(u'псевдоним'),help_text="не менять!", db_index=True, blank=True, null=True)
    in_menu = models.BooleanField(verbose_name=_(u'в верхнем меню?'),default=False)
    code = models.TextField(verbose_name=_(u'код для всавки'), blank=True, null=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = _(u'страница')
        verbose_name_plural = _(u'страницы')



class News(models.Model):
    title = models.CharField(max_length=250,verbose_name=_(u'заголовок'))
    image  = models.ImageField(upload_to='news', verbose_name=u'Изображение', blank=True, null=True)
    short_text = models.TextField(verbose_name=_(u'короткое описание'), blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    slug = models.CharField(max_length=50,verbose_name=_(u'URL'),help_text="генерируется автоматически!", db_index=True, blank=True, null=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
       return reverse("news", kwargs={"slug": self.slug})
    def save(self, **kwargs):
        if not self.id:
            self.slug = pytils.translit.slugify(self.title)
        return super(News, self).save(**kwargs)
    class Meta:
        verbose_name = _(u'новость')
        verbose_name_plural = _(u'новости')


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
    code = models.TextField(verbose_name=_(u'код для вставки видео'), blank=True, null=True)
    video  = models.FileField(upload_to='video', verbose_name=u'Видеофайл', blank=True, null=True)
    def get_absolute_url(self):
        return reverse('film_detail', args=[self.id])
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
        
        
class Message(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'имя'))
    text = models.TextField(verbose_name=_(u'описание'))
    is_published = models.BooleanField(verbose_name=_(u'опубликован?'),default=False)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _(u'Отзыв')
        verbose_name_plural = _(u'Отзывы')    

class Videos(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='video', verbose_name=u'Изображение', blank=True, null=True)
    code = models.TextField(verbose_name=_(u'код для вставки'), blank=True, null=True)
    video  = models.FileField(upload_to='video', verbose_name=u'Видео', blank=True, null=True)
    ftp = models.CharField(verbose_name=_(u'имя на фтп'), max_length=250, blank=True, null=True)

    @property
    def is_ftp(self):
        if len(self.ftp)>2:
            return True
        else:
            return False



class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'заголовок'))
    shorttext = models.TextField(verbose_name=_(u'краткое описание'), blank=True, null=True)
    text = RichTextField(verbose_name=_(u'описание'), blank=True, null=True)
    image  = models.ImageField(upload_to='blog', verbose_name=u'Изображение', blank=True, null=True)
    cropping = ImageRatioField('image', '180x180')
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])
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
