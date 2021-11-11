from django.urls import path
from hello import views

urlpatterns = [
    path("buildings/create/", views.BuildingCreate.as_view()),
    path("buildings/", views.BuildingList.as_view()),
    path("buildings/<pk>/", views.BuildingDetails.as_view()),
]