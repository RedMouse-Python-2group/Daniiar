from urllib.parse import quote_plus #https://docs.djangoproject.com/en/1.9/ref/utils/
from django import template

register = template.Library()

@register.filter
def urlify(value):
    return quote_plus(value)

