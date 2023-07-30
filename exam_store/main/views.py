from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse


from exam_store.main.models import ProductModel


# Create your views here.

class CatalogueView(TemplateView, LoginRequiredMixin):
    template_name = 'main/catalogue_page.html'
    model = ProductModel
    products = ProductModel.objects.all()
    extra_context = {
        "products": products,
    }


class AboutPageView(TemplateView):
    template_name = "main/about_page.html"


class HomePageView(TemplateView):
    template_name = 'main/home_page.html'


class ShoppingCartView(TemplateView):
    template_name = 'main/shopping_cart.html'


def search_view(request):
    query = request.GET.get('q', '').strip()
    # Perform your search logic here based on the query and return the results as a list of dictionaries
    # For simplicity, we'll just return a sample list of results.
    products = ProductModel.objects.all()
    results = [
        products
    ]
    return JsonResponse(results, safe=False)
