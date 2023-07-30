from django.db import models
from django.contrib.auth.models import User
from exam_store.main.validators import validate_starts_with_uppercase
from django.core.validators import MinLengthValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=40, validators=[
        MinLengthValidator(3), validate_starts_with_uppercase
    ])
    description = models.TextField(blank=True, max_length=300)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    age = models.IntegerField()
    # Add more fields as needed
