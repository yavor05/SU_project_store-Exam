from django.db import models
from django.contrib.auth import get_user_model
from exam_store.main.validators import validate_starts_with_uppercase
from django.core.validators import MinLengthValidator

User = get_user_model()


class CategoryModel(models.Model):
    name = models.CharField(
        max_length=20,
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


class ProductModel(models.Model):
    name = models.CharField(
        max_length=20,
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
    image = models.ImageField()
    category = models.ForeignKey(to=CategoryModel)
    quantity = models.IntegerField(default=0)


class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity
