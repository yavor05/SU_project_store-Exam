from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from exam_store.auth_app.models import UserProfile
from exam_store.main.models import ProductModel, CartItem


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


@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    context = {
        'products': cart_items
    }

    return render(request=request, template_name='main/shopping_cart.html', context=context)


def search_results(request):
    query = request.GET.get('q', '')
    products = ProductModel.objects.filter(name__icontains=query)
    context = {'products': products, 'query': query}
    return render(request=request, template_name='products/search_results.html', context=context)
