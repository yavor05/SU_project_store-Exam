from django.urls import path
from .views import HomePageView, AboutPageView, view_cart, search_results

urlpatterns = (
    path('', HomePageView.as_view(), name='home_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('cart/', view_cart, name='shopping_cart'),
    path('search/', search_results, name='search_results'),
)
