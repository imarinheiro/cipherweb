from django import template
import numpy as np
from s_aes.utils import string_to_array

register = template.Library()


@register.simple_tag
def bin_to_dec(array):
    return [int(x, 2) for x in array]


@register.simple_tag
def bin(x):
    return np.binary_repr(x)


@register.simple_tag
def tuple_before_after(dict):
    t = []
    for i, x in enumerate(dict['before']):
        t.append((x, dict['after'][i]))
    return t


@register.simple_tag
def round_key_state(key_array, round):
    key = key_array[2 * round] + key_array[2 * round + 1]
    return string_to_array(key)


@register.simple_tag
def name_to_label(form, key):
    return form.fields.get(key).label
