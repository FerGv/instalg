from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers

from apps.materiales.models import Material
from .models import Pedido, Item
from .forms import PedidoForm


class PedidoCreate(CreateView):
    template_name = 'pedidos/form.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materiales = Material.objects.all()
        context['materiales'] = materiales
        context['materiales_json'] = serializers.serialize('json', list(materiales), fields=('nombre',))
        return context

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        form = self.form_class(request.POST)

        if form.is_valid():
            pedido = form.save()
            subtotal_pedido = 0
            
            for material,cantidad in zip(request.POST.pop('materiales'), request.POST.pop('cantidades')):
                material = Material.objects.get(pk=material)
                importe = float(cantidad) * material.precio
                subtotal_pedido += importe
                item = Item(pedido=pedido, material=material, precio_unitario=material.precio, cantidad=float(cantidad), importe=importe)
                item.save()

            pedido.subtotal = subtotal_pedido
            pedido.iva = subtotal_pedido * 0.16
            pedido.total = subtotal_pedido * 1.16
            pedido.save()

            return redirect('pedidos:detail', pk=pedido.pk)

        return render(request, self.template_name, {'form': form})

class PedidoUpdate(UpdateView):
    model = Pedido
    template_name = 'pedidos/form.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materiales = Material.objects.all()
        context['materiales'] = materiales
        context['materiales_json'] = serializers.serialize('json', list(materiales), fields=('nombre',))
        return context

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        pedido = self.get_object()
        form = self.form_class(request.POST, instance=pedido)

        if form.is_valid():
            form.save()
            pedido.materiales.clear()
            subtotal_pedido = 0

            for material,cantidad in zip(request.POST.pop('materiales'), request.POST.pop('cantidades')):
                material = Material.objects.get(pk=material)
                importe = float(cantidad) * material.precio
                subtotal_pedido += importe
                item = Item(pedido=pedido, material=material, precio_unitario=material.precio, cantidad=float(cantidad), importe=importe)
                item.save()

            pedido.subtotal = subtotal_pedido
            pedido.iva = subtotal_pedido * 0.16
            pedido.total = subtotal_pedido * 1.16
            pedido.save()

            return redirect('pedidos:detail', pk=pedido.pk)

        return render(request, self.template_name, {'form': form})
    
class PedidoList(ListView):
    model = Pedido
    template_name = 'pedidos/list.html'

class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'pedidos/detail.html'

class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedidos/delete.html'
    success_url = reverse_lazy('pedidos:list')
