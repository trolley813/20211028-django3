import uuid
from django.db import models

# Create your models here.
class BuildingSeries(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"Series {self.name} ({self.id})"


class Building(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    address = models.CharField(max_length=128)
    floor_count = models.IntegerField()
    build_date = models.DateField()
    series = models.ForeignKey(BuildingSeries, on_delete=models.SET_NULL, null=True, blank=True)