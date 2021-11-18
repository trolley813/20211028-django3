from django.urls import path
from hello import views

urlpatterns = [
    path("buildings/create/", views.BuildingCreate.as_view()),
    path("buildings/", views.BuildingList.as_view()),
    path("buildings/<pk>/", views.BuildingDetails.as_view()),
    path("buildings/<pk>/edit", views.BuildingUpdate.as_view()),
    path("buildings/<pk>/delete", views.BuildingDelete.as_view()),

    path("building_series/create/", views.BuildingSeriesCreate.as_view()),
    path("building_series/", views.BuildingSeriesList.as_view()),
    path("building_series/<pk>/", views.BuildingSeriesDetails.as_view()),
    path("building_series/<pk>/edit", views.BuildingSeriesUpdate.as_view()),
    path("building_series/<pk>/delete", views.BuildingSeriesDelete.as_view()),
]