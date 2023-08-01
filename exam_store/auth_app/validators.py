from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator


def password_complexity_validator(value):
    min_length_validator = MinLengthValidator(8, message='Password must be at least 8 characters long.')
    numeric_validator = RegexValidator(regex=r'[0-9]', message='Password must contain at least one numeric character.')
    alphabetic_validator = RegexValidator(regex=r'[a-zA-Z]',
                                          message='Password must contain at least one alphabetic character.')
    special_character_validator = RegexValidator(regex=r'[!@#$%^&*(),.?":{}|<>]',
                                                 message='Password must contain at least one special character.')

    min_length_validator(value)
    numeric_validator(value)
    alphabetic_validator(value)
    special_character_validator(value)

def letters_only_validator(value):
    if not value.isalpha():
        raise ValidationError('Only letters are allowed.')

