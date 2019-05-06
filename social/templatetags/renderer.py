from contextlib import contextmanager
from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen

from django import template
from django.template.loader import render_to_string
from purima.utils.get_preview import get_preview

register = template.Library()


@register.filter
def get_class(item):
    return item.__class__.__name__.lower()


@register.simple_tag
def as_html(item):
    result = render_to_string(
        f"repr/{item.__class__.__name__.lower()}.html", {"item": item}
    )
    return result


register.simple_tag(get_preview)
