from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', UserList.as_view(), name='list'),
    url(r'^create/$', UserCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', UserDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', UserDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', UserUpdate.as_view(), name='update'),
]
