from django.core.exceptions import ValidationError
from sympy import isprime


def validate_is_prime(value):
    if not isprime(value):
        raise ValidationError('{} is not an prime number valid'.format(value))


def validate_message_length(value):
    if len(value) > 1 and value.isalpha():
        raise ValidationError('{} is not an text valid'.format(value))
    elif len(value) > 1 and not value.isdigit():
        raise ValidationError('{} is not only numbers'.format(value))
