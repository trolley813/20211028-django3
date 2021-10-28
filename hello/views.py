from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, id):
    return HttpResponse(f"{id} * {id} = {id * id}")