from django.core.exceptions import ValidationError


def validate_starts_with_uppercase(value):
    if not value[0].isupper():
        raise ValidationError("String must start with an uppercase letter.")
