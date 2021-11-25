from django.urls import path
from hello import views

urlpatterns = [
    path("buildings/create/", views.BuildingCreate.as_view(), name="building-create"),
    path("buildings/", views.BuildingList.as_view(), name="building-list"),
    path("buildings/<pk>/", views.BuildingDetails.as_view(), name="building-details"),
    path("buildings/<pk>/edit", views.BuildingUpdate.as_view(), name="building-update"),
    path("buildings/<pk>/delete", views.BuildingDelete.as_view(), name="building-delete"),

    path("building_series/create/", views.BuildingSeriesCreate.as_view(), name="series-create"),
    path("building_series/", views.BuildingSeriesList.as_view(), name="series-list"),
    path("building_series/<pk>/", views.BuildingSeriesDetails.as_view(), name="series-details"),
    path("building_series/<pk>/edit", views.BuildingSeriesUpdate.as_view(), name="series-update"),
    path("building_series/<pk>/delete", views.BuildingSeriesDelete.as_view(), name="series-delete"),
]