from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from .forms import UserForm


class UserCreate(CreateView):
    model = User
    template_name = 'usuarios/form.html'
    # form_class = UserForm
    success_url = reverse_lazy('usuarios:list')

class UserUpdate(UpdateView):
    model = User
    template_name = 'usuarios/form.html'
    # form_class = UserForm
    success_url = reverse_lazy('usuarios:list')
    
class UserList(ListView):
    model = User
    template_name = 'usuarios/list.html'

class UserDetail(DetailView):
    model = User
    template_name = 'usuarios/detail.html'

class UserDelete(DeleteView):
    model = User
    template_name = 'usuarios/delete.html'
    success_url = reverse_lazy('usuarios:list')
