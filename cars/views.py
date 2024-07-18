from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView , CreateView, DetailView, UpdateView, DeleteView
from django.contrib import admin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth. decorators import login_required
from django.utils.decorators import method_decorator



class CarListView(ListView):
    model = Car 
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self): 
       
        cars = super().get_queryset().order_by('model') 
        search = self.request.GET.get('search') 

        if search: 
            cars = cars.filter(
                Q( model__icontains=search ) | Q( brand__model__icontains=search )
                )
                 
        return cars 

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'  
    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm 
    template_name = 'new_car.html'
    success_url = '/cars/' 


@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm # vai mostrar para o user uma tela de cadastro igual a de cadastrar novo carro
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_datail', kwargs={'pk': self.object.pk})
@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'