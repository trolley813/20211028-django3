from django import forms
from django.forms import models
from hello.models import Building

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ["address", "floor_count", "build_date"]