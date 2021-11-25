from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from hello.models import Building, BuildingSeries

class BuildingSeriesCreate(CreateView):
    model = BuildingSeries

    fields = ["name"]

    success_url = reverse_lazy("series-list")

class BuildingSeriesList(ListView):
    model = BuildingSeries

class BuildingSeriesDetails(DetailView):
    model = BuildingSeries

class BuildingSeriesUpdate(UpdateView):
    model = BuildingSeries

    fields = ["name"]

class BuildingSeriesDelete(DeleteView):
    model = BuildingSeries

    success_url = reverse_lazy("series-list")

class BuildingCreate(CreateView):
    model = Building

    fields = ["address", "floor_count", "build_date", "series"]

    success_url = reverse_lazy("building-list")

class BuildingList(ListView):
    model = Building

class BuildingDetails(DetailView):
    model = Building

class BuildingUpdate(UpdateView):
    model = Building

    fields = ["address", "floor_count", "build_date", "series"]

class BuildingDelete(DeleteView):
    model = Building

    success_url = reverse_lazy("building-list")