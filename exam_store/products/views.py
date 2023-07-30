from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, \
    DeleteView, DetailView

from exam_store.main.models import ProductModel


# Create your views here.
class AddProductView(FormView):
    form_class = ProductModel
    template_name = 'products/add_product.html'


class EditProductView(UpdateView):
    model = ProductModel
    template_name = 'products/edit_product.html'
    fields = '__all__'
    success_url = reverse_lazy('catalogue_page')


class DeleteProductView(DeleteView):
    template_name = 'products/delete_product.html'
    model = ProductModel
    success_url = reverse_lazy('catalogue_page')


class DetailProductView(DetailView):
    template_name = 'products/details_product.html'
    model = ProductModel
    context_object_name = 'product'


class ClothesCatalogue(TemplateView):
    template_name = "products/clothes_catalogue.html"


class ShoesCatalogue(TemplateView):
    template_name = "products/shoes_catalogue.html"


class AccessoriesCatalogue(TemplateView):
    template_name = "products/accessories_catalogue.html"
