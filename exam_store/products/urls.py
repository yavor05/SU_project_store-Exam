from django.urls import path
from .views import ClothesCatalogue, ShoesCatalogue, AccessoriesCatalogue, CatalogueView, delete_product, \
    DetailProductView, add_product_view, edit_product_view,  add_to_cart, checkout

urlpatterns = (
    path("clothes/", ClothesCatalogue.as_view(), name="clothes_catalogue"),
    path("shoes/", ShoesCatalogue.as_view(), name="shoes_catalogue"),
    path("accessories/", AccessoriesCatalogue.as_view(), name="accessories_catalogue"),
    path('catalogue/', CatalogueView.as_view(), name='catalogue_page'),
    path('details/<int:pk>/', DetailProductView.as_view(), name='product_detail_page'),
    path('delete/<int:pk>/', delete_product, name='product_delete_page'),
    path('add/', add_product_view, name='product_add_page'),
    path('edit/<int:pk>/', edit_product_view, name='product_edit_page'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),

)
