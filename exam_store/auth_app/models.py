from django.db import models
from django.contrib.auth import models as auth_models
from .validators import letters_only_validator
from exam_store.main.validators import validate_starts_with_uppercase
from django.core.validators import MinLengthValidator


class UserProfile(auth_models.AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    first_name = models.CharField(blank=False, null=False, max_length=40, validators=[
        MinLengthValidator(2), validate_starts_with_uppercase, letters_only_validator
    ])
    last_name = models.CharField(blank=False, null=False, max_length=40, validators=[
        MinLengthValidator(2), validate_starts_with_uppercase, letters_only_validator
    ])
    description = models.TextField(blank=True, max_length=300)
    profile_picture = models.ImageField(upload_to='avatars/', blank=True, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"I am {self.first_name} {self.last_name}"
