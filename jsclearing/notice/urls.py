from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

from models import Story


urlpatterns = patterns('jsclearing.notice.views',
    url(r'^(?P<slug>[-\w]+)/$', 'notice_detail',name='cms-story'),
)

urlpatterns += patterns('jsclearing.notice.views',
    url(r'^category/(?P<slug>[-\w]+)/$', 'category', name="cms-category"),
#    url(r'^search/$', 'search', name="cms-search"),
)

