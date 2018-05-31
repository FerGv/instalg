from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Empleado
from .forms import EmpleadoForm


class EmpleadoCreate(CreateView):
    template_name = 'empleados/form.html'
    form_class = EmpleadoForm
    # success_url = reverse_lazy('empleados:list')

    def form_valid(self, form):
        empleado = form.save()
        user = User.objects.create(empleado.numero, empleado.email, empleado.email)
        user.first_name = empleado.nombre
        user.last_name = empleado.apellido_paterno
        user.save()
        empleado.user = user
        empleado.save()
        return redirect('empleados:detail', pk=empleado.pk)

class EmpleadoUpdate(UpdateView):
    model = Empleado
    template_name = 'empleados/form.html'
    form_class = EmpleadoForm
    # success_url = reverse_lazy('empleados:list')

    def form_valid(self, form):
        form.save()
        empleado = self.get_object()
        empleado.user.username = empleado.numero
        empleado.user.email = empleado.email
        empleado.user.set_password(empleado.email)
        empleado.user.first_name = empleado.nombre
        empleado.user.last_name = empleado.apellido_paterno
        empleado.user.save()
        # empleado.save()
        return redirect('empleados:detail', pk=empleado.pk)
    
class EmpleadoList(ListView):
    model = Empleado
    template_name = 'empleados/list.html'

class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = 'empleados/detail.html'

class EmpleadoDelete(DeleteView):
    model = Empleado
    template_name = 'empleados/delete.html'
    success_url = reverse_lazy('empleados:list')
