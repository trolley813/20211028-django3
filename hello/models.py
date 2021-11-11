from django.db import models

# Create your models here.
class Building(models.Model):
    address = models.CharField(max_length=128)
    floor_count = models.IntegerField()
    build_date = models.DateField()