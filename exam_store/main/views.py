from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import JsonResponse

from exam_store.auth_app.models import UserProfile
from exam_store.main.models import ProductModel


# Create your views here.


class AboutPageView(TemplateView):
    template_name = "main/about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context

class HomePageView(TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class ShoppingCartView(TemplateView):
    template_name = 'main/shopping_cart.html'

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        context = {
            "profile": current_user,
            "pk": current_user.pk
        }
        return render(request, template_name='main/shopping_cart.html', context=context)


def search_view(request):
    query = request.GET.get('q', '').strip()
    # Perform your search logic here based on the query and return the results as a list of dictionaries
    # For simplicity, we'll just return a sample list of results.
    products = ProductModel.objects.all()
    results = [
        products
    ]
    return JsonResponse(results, safe=False)
