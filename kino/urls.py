from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from main.views import NewsListView, NewsDetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.index', name='home'),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^news/list$', NewsListView.as_view()),
    url(r'^news/(?P<slug>[^\.]+).html$', NewsDetailView.as_view(), name='news'),

    url(r'^page/(?P<id>[^\.]+).html', 'main.views.page', name='page_detail'),
    url(r'^festival/(?P<id>[^\.]+).html', 'main.views.festival', name='festival_detail'),
    url(r'^film/(?P<id>[^\.]+).html', 'main.views.film', name='film_detail'),
    url(r'^blog/(?P<id>[^\.]+).html', 'main.views.blog', name='blog_detail'),
    
    url(r'^api/vote', 'main.views.vote', name='film_detail'),
     
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
