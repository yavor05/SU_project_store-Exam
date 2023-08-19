import sys

from django.db import models
from django.contrib.auth import get_user_model
from exam_store.main.validators import validate_starts_with_uppercase
from django.core.validators import MinLengthValidator
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

User = get_user_model()


class ProductModel(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('clothes', 'Clothes'),
        ('accessories', 'Accessories'),
    ]
    name = models.CharField(
        max_length=100,
        validators=
        [
            validate_starts_with_uppercase,
            MinLengthValidator(3),
        ]

    )
    description = models.TextField(
        max_length=500,
        validators=
        [
            validate_starts_with_uppercase,
            MinLengthValidator(10),
        ]
    )
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField(default=0)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)




class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1-1')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name
