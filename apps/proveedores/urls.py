from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', login_required(ProveedorList.as_view()), name='list'),
    url(r'^create/$', login_required(ProveedorCreate.as_view()), name='create'),
    url(r'^(?P<pk>\w+)/$', login_required(ProveedorDetail.as_view()), name='detail'),
    url(r'^(?P<pk>\w+)/delete/$', login_required(ProveedorDelete.as_view()), name='delete'),
    url(r'^(?P<pk>\w+)/update/$', login_required(ProveedorUpdate.as_view()), name='update'),
]
