from django.urls import path
from .views import home, save_data, delete_data


urlpatterns = [
    path("", home, name="home"),
    path("save/", save_data, name="save"),
    path("delete/", delete_data, name="delete"),
]