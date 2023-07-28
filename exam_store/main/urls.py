from django.urls import path
from .views import CatalogueView, HomePageView

urlpatterns = (
    path('', HomePageView.as_view, name='home_page'),
    path('catalogue/', CatalogueView.as_view, name='catalogue_page'),
)
