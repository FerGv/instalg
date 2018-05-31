from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', login_required(InstalacionList.as_view()), name='list'),
    url(r'^create/$', login_required(InstalacionCreate.as_view()), name='create'),
    url(r'^(?P<pk>\w+)/$', login_required(InstalacionDetail.as_view()), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', login_required(InstalacionDelete.as_view()), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', login_required(InstalacionUpdate.as_view()), name='update'),
]
