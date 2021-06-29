from django.template.defaulttags import register
from django import template

register = template.Library()


@register.filter(name='get_energy')
def get_energy(dictionary: dict, key):
    return dictionary.get(key)['energy']


@register.filter(name='get_power')
def get_power(dictionary: dict, key):
    return dictionary.get(key)['power']


@register.filter(name='get_error')
def get_error(dictionary: dict, key):
    return dictionary.get(key)['error']
