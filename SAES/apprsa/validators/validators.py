from django.core.exceptions import ValidationError
from sympy import isprime


def validate_is_prime(value):
    if not isprime(value):
        raise ValidationError('{} Não é um número primo.'.format(value))


def validate_message_length(value):
    if len(value) > 1 and value.isalpha():
        raise ValidationError('{} não é um texto válido.'.format(value))
    elif len(value) > 1 and not value.isdigit():
        raise ValidationError('{} não é apenas números.'.format(value))
