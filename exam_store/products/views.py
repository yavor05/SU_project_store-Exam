from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, \
    DeleteView, DetailView

from exam_store.auth_app.models import UserProfile
from exam_store.main.models import ProductModel

def is_staff(user):
    return user.role == 'staff'

def is_user(user):
    return user.role == 'user'
# Create your views here.
class AddProductView(FormView):
    form_class = ProductModel
    template_name = 'products/add_product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context

class EditProductView(UpdateView):
    model = ProductModel
    template_name = 'products/edit_product.html'
    fields = '__all__'
    success_url = reverse_lazy('catalogue_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class DeleteProductView(DeleteView):
    template_name = 'products/delete_product.html'
    model = ProductModel
    success_url = reverse_lazy('catalogue_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class DetailProductView(DetailView):
    template_name = 'products/details_product.html'
    model = ProductModel
    context_object_name = 'product'
    shoes = ProductModel.objects.filter(category="shoes")
    clothes = ProductModel.objects.filter(category="clothes")
    accessories = ProductModel.objects.filter(category="accessories")
    extra_context = {
        'shoes': shoes,
        'clothes': clothes,
        'accessories': accessories,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class ClothesCatalogue(TemplateView):
    template_name = "products/clothes_catalogue.html"
    clothes = ProductModel.objects.filter(category="clothes")
    extra_context = {
        'products': clothes
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class ShoesCatalogue(TemplateView):
    template_name = "products/shoes_catalogue.html"
    shoes = ProductModel.objects.filter(category="shoes")
    extra_context = {
        'products': shoes
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class AccessoriesCatalogue(TemplateView):
    template_name = "products/accessories_catalogue.html"
    accessories = ProductModel.objects.filter(category="accessories")
    extra_context = {
        'products': accessories
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to pass the logged-in user's profile to the context
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(pk=self.request.user.pk)
            context['profile'] = profile

        return context


class CatalogueView(TemplateView, LoginRequiredMixin):
    template_name = 'products/catalogue_page.html'
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
            "profile": current_user,
            "pk": current_user.id
        }
        return render(request, template_name='products/catalogue_page.html', context=context)
