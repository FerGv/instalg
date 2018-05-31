from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', login_required(PuestoList.as_view()), name='list'),
    url(r'^create/$', login_required(PuestoCreate.as_view()), name='create'),
    url(r'^(?P<pk>\w+)/$', login_required(PuestoDetail.as_view()), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', login_required(PuestoDelete.as_view()), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', login_required(PuestoUpdate.as_view()), name='update'),
]
