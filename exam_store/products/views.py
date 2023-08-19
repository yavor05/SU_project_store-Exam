from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, \
    DeleteView, DetailView

from exam_store.auth_app.models import UserProfile
from exam_store.main.models import ProductModel, Cart
from django.contrib.auth.decorators import user_passes_test

from exam_store.products.forms import ProductModelForm, DeleteProductForm, ProductEditForm
from exam_store.main.models import ProductModel, CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    user = request.user  # Assuming you're using the built-in authentication system
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, user=user, product=product)
    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shopping_cart')  # Redirect to the product detail page





def add_product_view(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Redirect to home page after adding a product
    else:
        form = ProductModelForm()

    context = {}
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(pk=request.user.pk)
        context['profile'] = profile

    context['form'] = form
    return render(request, 'products/add_product.html', context)


def edit_product_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Redirect to home page after editing the product
    else:
        form = ProductEditForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'products/edit_product.html', context)


def delete_product(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)

    if request.method == 'POST':
        form = DeleteProductForm(request.POST, instance=product)
        if form.is_valid():
            product.delete()
            return redirect('home_page')  # Redirect to home page after deletion
    else:
        form = DeleteProductForm(instance=product)

    return render(request, 'products/delete_product.html', {'form': form, 'product': product})


class DetailProductView(DetailView, LoginRequiredMixin):
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


class ClothesCatalogue(TemplateView, LoginRequiredMixin):
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


class ShoesCatalogue(TemplateView, LoginRequiredMixin):
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


class AccessoriesCatalogue(TemplateView, LoginRequiredMixin):
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
