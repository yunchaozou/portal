from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jsclearing.views.home', name='home'),
    url(r'^about_us$', 'jsclearing.views.about_us', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
  #  url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    url(r'^poll/', include('jsclearing.poll.urls')),
    url(r'^notice/', include('jsclearing.notice.urls')),
    url(r'^info_center$', 'jsclearing.views.info_center', name='info'),
    url(r'^recruitment$', 'jsclearing.views.recruitment', name='recruitment'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^search$', 'jsclearing.views.search', name='search'),
)
from jsclearing.settings import DEBUG
from django.conf.urls.static import static
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)