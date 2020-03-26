from django import template

register = template.Library()


@register.simple_tag
def generate_range(a, b):
    return [x for x in range(2, min(a, b) + 1)]


@register.simple_tag
def string_to_decimal_ascii(char: str):
    return ord(char)
