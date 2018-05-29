from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', ClienteList.as_view(), name='list'),
    url(r'^create/$', ClienteCreate.as_view(), name='create'),
    url(r'^(?P<pk>\w+)/$', ClienteDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', ClienteDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', ClienteUpdate.as_view(), name='update'),
]
