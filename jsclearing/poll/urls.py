#from newtest.address.models import Address
from django.conf.urls import url

from jsclearing.poll import views
urlpatterns =[
#    url(r'^$', 'newtest.poll.views.index', name='index'),
 #   url(r'^(?P<poll_id>\d+)/$', 'newtest.poll.views.detail', name='detail'),
#    url(r'^(?P<poll_id>\d+)/results/$', 'newtest.poll.views.results', name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'jsclearing.poll.views.vote', name='vote'),
    #generic view
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
]