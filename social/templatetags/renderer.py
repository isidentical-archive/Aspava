from urllib.parse import urlparse

from django import template
from django.template.loader import render_to_string
from purima.utils.get_preview import _get_preview, construct_preview

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


@register.simple_tag
def get_preview(url):
    try:
        preview = _get_preview(url)
    except:
        _url = urlparse(url)
        preview = construct_preview(url, {'title': _url.netloc})
    
    return preview
