from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, \
    DeleteView, DetailView
from django.conf import settings

from exam_store.auth_app.models import UserProfile
from exam_store.main.models import ProductModel, Cart
from django.contrib.auth.decorators import user_passes_test

from exam_store.products.forms import ProductModelForm, DeleteProductForm, ProductEditForm, CheckoutForm
from exam_store.main.models import ProductModel, CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)
    user = request.user
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1  # !!!!
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
        profile = UserProfile.objects.filter(pk=request.user.pk).first()
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
            profile = UserProfile.objects.filter(pk=self.request.user.pk).first()
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
            profile = UserProfile.objects.filter(pk=self.request.user.pk).first()
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
            profile = UserProfile.objects.filter(pk=self.request.user.pk).first()
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
            profile = UserProfile.objects.filter(pk=self.request.user.pk).first()
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


class CheckoutView(FormView):
    template_name = 'products/checkout_page.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('order_thank_you')

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        city = form.cleaned_data['city']
        address = form.cleaned_data['address']
        payment_method = form.cleaned_data['payment_method']

        message = render_to_string('email/order_confirmation_email.txt',
                                   {'full_name': full_name, 'email': email, 'city': city, 'address': address,
                                    'payment_method': payment_method})

        # Send email
        send_mail(
            'Order Confirmation',  # Subject
            message,  # Message
            settings.EMAIL_HOST_USER,  # From email
            [email],  # To email
            fail_silently=False,
        )

        # Further processing or redirecting logic
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('shopping_cart')


def order_thank_you(request):
    return render(request=request, template_name='products/order_thank_you.html')

