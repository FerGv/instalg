from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cliente
from .forms import ClienteForm


class ClienteCreate(CreateView):
    template_name = 'clientes/form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')

class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'clientes/form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')
    
class ClienteList(ListView):
    model = Cliente
    template_name = 'clientes/list.html'

class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'clientes/detail.html'

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'clientes/delete.html'
    success_url = reverse_lazy('clientes:list')
