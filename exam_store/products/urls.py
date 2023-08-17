from django.urls import path
from .views import ClothesCatalogue, ShoesCatalogue, AccessoriesCatalogue, CatalogueView, DeleteProductView, DetailProductView

urlpatterns = (
    path("clothes/", ClothesCatalogue.as_view(), name="clothes_catalogue"),
    path("shoes/", ShoesCatalogue.as_view(), name="shoes_catalogue"),
    path("accessories/", AccessoriesCatalogue.as_view(), name="accessories_catalogue"),
    path('catalogue/', CatalogueView.as_view(), name='catalogue_page'),
    path('details/<int:pk>/', DetailProductView.as_view(), name='product_detail_page'),

)
