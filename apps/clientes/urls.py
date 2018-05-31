from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', login_required(ClienteList.as_view()), name='list'),
    url(r'^create/$', login_required(ClienteCreate.as_view()), name='create'),
    url(r'^(?P<pk>\w+)/$', login_required(ClienteDetail.as_view()), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', login_required(ClienteDelete.as_view()), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', login_required(ClienteUpdate.as_view()), name='update'),
]
