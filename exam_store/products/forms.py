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