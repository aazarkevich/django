from django.template.defaulttags import register
from django import template

register = template.Library()


@register.filter(name='get_substation')
def get_substation(substations, id_substation):
    try:
        return substations.filter(id=id_substation).first()
    except ValueError:
        return
