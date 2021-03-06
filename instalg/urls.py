from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', login_required(TemplateView.as_view(template_name="index.html")), name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^clientes/', include('apps.clientes.urls', namespace="clientes")),
    url(r'^empleados/', include('apps.empleados.urls', namespace="empleados")),
    url(r'^instalaciones/', include('apps.instalaciones.urls', namespace="instalaciones")),
    url(r'^materiales/', include('apps.materiales.urls', namespace="materiales")),
    url(r'^pedidos/', include('apps.pedidos.urls', namespace="pedidos")),
    url(r'^proveedores/', include('apps.proveedores.urls', namespace="proveedores")),
    url(r'^puestos/', include('apps.puestos.urls', namespace="puestos")),
    url(r'^usuarios/', include('apps.usuarios.urls', namespace="users")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
