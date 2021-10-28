from django.urls import path
from hello import views

urlpatterns = [
    path("hello/<int:id>", views.home, name="home"),
]