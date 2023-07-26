from django.views.generic.list import ListView
from django.shortcuts import render

# Create your views here.

class CatalogueView(ListView):
    template_name = 'catalogue page'
    model = ProductModel