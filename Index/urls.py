from django.urls import path
from Index.views import index, paletas

urlpatterns = [
    path("", index),
    path("paletas/", paletas)
]

