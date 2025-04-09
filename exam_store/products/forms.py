from django import forms

from exam_store.main.models import ProductModel


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'


class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = []


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'description', 'price', 'image', 'category', 'quantity']


class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    payment_method = forms.ChoiceField(choices=
    [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('on_delivery', 'On delivery')
    ]
    )

