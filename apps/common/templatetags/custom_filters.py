from urllib.parse import urlencode
from django import template

register = template.Library()

@register.filter
def dict_to_query_string(value):
    return urlencode([tup for tup in list(value.items()) if 'page' not in tup[0]])
