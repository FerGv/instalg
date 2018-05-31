from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Proveedor
from .forms import ProveedorForm


class ProveedorCreate(CreateView):
    template_name = 'proveedores/form.html'
    form_class = ProveedorForm
    # success_url = reverse_lazy('proveedores:list')

    def form_valid(self, form):
        proveedor = form.save()
        user = User.objects.create(proveedor.numero, proveedor.email, proveedor.email)
        user.first_name = proveedor.nombre
        user.last_name = proveedor.apellido_paterno
        user.save()
        proveedor.user = user
        proveedor.save()
        return redirect('proveedores:detail', pk=proveedor.pk)

class ProveedorUpdate(UpdateView):
    model = Proveedor
    template_name = 'proveedores/form.html'
    form_class = ProveedorForm
    # success_url = reverse_lazy('proveedores:list')

    def form_valid(self, form):
        form.save()
        proveedor = self.get_object()
        proveedor.user.username = proveedor.numero
        proveedor.user.email = proveedor.email
        proveedor.user.set_password(proveedor.email)
        proveedor.user.first_name = proveedor.nombre
        proveedor.user.last_name = proveedor.apellido_paterno
        proveedor.user.save()
        # proveedor.save()
        return redirect('proveedores:detail', pk=proveedor.pk)
    
class ProveedorList(ListView):
    model = Proveedor
    template_name = 'proveedores/list.html'

class ProveedorDetail(DetailView):
    model = Proveedor
    template_name = 'proveedores/detail.html'

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'proveedores/delete.html'
    success_url = reverse_lazy('proveedores:list')
