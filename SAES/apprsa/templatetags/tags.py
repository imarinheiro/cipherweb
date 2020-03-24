from django import template

register = template.Library()


@register.simple_tag
def teste(array):
    return None

