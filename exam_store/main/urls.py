from django.urls import path
from .views import CatalogueView, HomePageView, AboutPageView, ShoppingCartView, search_view

urlpatterns = (
    path('', HomePageView.as_view(), name='home_page'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('cart/', ShoppingCartView.as_view(), name='shopping_cart'),
    path('search/', search_view, name='search_view')
)
