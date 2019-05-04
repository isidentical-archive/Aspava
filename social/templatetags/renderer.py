from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def as_html(item):
    result = render_to_string(f"repr/{item.__class__.__name__.lower()}.html", {'item': item})
    return result 
