"""
https://docs.djangoproject.com/en/2.2/ref/templates/builtins/
"""

from django import template

register = template.Library()


@register.filter
def arredondamento(value, casas):
    return round(value, casas)
# {{ 00.0000|arredondamento:2 }}