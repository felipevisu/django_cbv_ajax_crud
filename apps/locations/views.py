from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import *


class CityListView(ListView):
    model = City


class SectorInline(InlineFormSetFactory):
    model = Sector
    fields = ['name']
    factory_kwargs = {'extra': 1}


class CityCreateView(CreateWithInlinesView):
    model = City
    fields = ['name']
    inlines = [SectorInline]
    success_url = reverse_lazy('locations:list')


class CityUpdateView(UpdateWithInlinesView):
    model = City
    fields = ['name']
    inlines = [SectorInline]
    success_url = reverse_lazy('locations:list')
