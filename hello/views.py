from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from hello.models import Building

class BuildingCreate(CreateView):
    model = Building

    fields = ["address", "floor_count", "build_date"]

    success_url = "/hello/buildings/"

class BuildingList(ListView):
    model = Building

class BuildingDetails(DetailView):
    model = Building