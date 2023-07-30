from django.urls import path
from .views import ClothesCatalogue, ShoesCatalogue, AccessoriesCatalogue
urlpatterns = (
    path("clothes/", ClothesCatalogue.as_view(), name="clothes_catalogue"),
    path("shoes/", ShoesCatalogue.as_view(), name="shoes_catalogue"),
    path("accessories/", AccessoriesCatalogue.as_view(), name="accessories_catalogue"),
)
