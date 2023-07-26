from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class User(UserModel):
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200, blank=True)
    order_history = models.ManyToManyField('Order', blank=True)
    payment_information = models.CharField(max_length=100, blank=True)

