from django.shortcuts import render
from .models import Car, Person
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.views import generic

# Create your views here.

class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/cars_detail.html'

class CarListView(generic.ListView):
    model = Car

    def get_queryset(self):
        return Car.objects.all()

class PersonListView(generic.ListView):
    model = Person

    def get_queryset(self):
        return Person.objects.all()

class CarDetailView(generic.DetailView):
    model = Car


class PersonDetailView(generic.DetailView):
    model = Person
