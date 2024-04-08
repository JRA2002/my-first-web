from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Item
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ItemListView(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'inventory/inventory.html'
class HomeView(TemplateView):
    template_name = 'inventory/home.html'
    
class UpdateItemView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/update_item.html'
    success_url = '/inventory/'
    
class DeleteItemView(DeleteView):
    model = Item
    template_name = 'inventory/delete_item.html'
    success_url = '/inventory/'
    
class CreateItemview(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/create_item.html'
    success_url = '/inventory/'
    
class OficinaView(TemplateView):
    template_name = 'inventory/oficina.html'
    

