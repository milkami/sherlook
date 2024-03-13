from urllib.parse import urlencode
from django import template

register = template.Library()

@register.filter
def dict_to_query_string(value):
    return urlencode(list(value.items()))