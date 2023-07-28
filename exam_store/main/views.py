from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render

from exam_store.main.models import ProductModel


# Create your views here.

class CatalogueView(TemplateView, LoginRequiredMixin):
    template_name = 'main/catalogue_page.html'
    model = ProductModel
    products = ProductModel.objects.all()
    extra_context = {
        "products": products,
    }


class HomePageView(TemplateView):
    template_name = 'main/home_page.html'
