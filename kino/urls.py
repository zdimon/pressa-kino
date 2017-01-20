from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.index', name='home'),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^page/(?P<id>[^\.]+).html', 'main.views.page', name='page_detail'),
    url(r'^festival/(?P<id>[^\.]+).html', 'main.views.festival', name='festival_detail'),
    url(r'^film/(?P<id>[^\.]+).html', 'main.views.film', name='film_detail'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
