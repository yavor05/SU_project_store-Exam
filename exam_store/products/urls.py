from django.urls import path
from .views import ClothesCatalogue, ShoesCatalogue, AccessoriesCatalogue, CatalogueView, delete_product, \
    DetailProductView, add_product_view, edit_product_view,  add_to_cart, CheckoutView , remove_from_cart, order_thank_you

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
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('order/',order_thank_you, name= 'order_thank_you'),

)
