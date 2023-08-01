from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import JsonResponse

from exam_store.auth_app.models import UserProfile
from exam_store.main.models import ProductModel


# Create your views here.

class CatalogueView(TemplateView, LoginRequiredMixin):
    template_name = 'main/catalogue_page.html'
    model = ProductModel
    products = ProductModel.objects.all()
    extra_context = {
        "products": products,
    }

    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        current_user = self.request.user
        context = {
            "products": products,
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


class AboutPageView(TemplateView):
    template_name = "main/about_page.html"

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


class HomePageView(View):
    template_name = 'main/home_page.html'

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


class ShoppingCartView(TemplateView):
    template_name = 'main/shopping_cart.html'

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user
        }
        return render(request, template_name='auth_app/profile_details.html', context=context)


def search_view(request):
    query = request.GET.get('q', '').strip()
    # Perform your search logic here based on the query and return the results as a list of dictionaries
    # For simplicity, we'll just return a sample list of results.
    products = ProductModel.objects.all()
    results = [
        products
    ]
    return JsonResponse(results, safe=False)
