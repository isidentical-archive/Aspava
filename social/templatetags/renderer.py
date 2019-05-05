from contextlib import contextmanager
from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen

from django import template
from django.template.loader import render_to_string

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


class MetaParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("property", "").startswith("og:"):
            self._meta[attrs["property"].strip("og:")] = attrs.get("content")


class SimpleHTMLConstructor:
    def __init__(self):
        self._buffer = StringIO()
        self._indent = 0

    def nl(self):
        self._buffer.write("\n")
        self._buffer.write(" " * 4 * self._indent)

    def write(self, *text):
        self._buffer.write("".join(text))
        self.nl()

    def ctx(self, *args, **kwds):
        with self.tag(*args, **kwds):
            pass

    @contextmanager
    def tag(self, tag, close=True, **attrs):
        attrs = self._strip_attrs(attrs)
        try:
            self._buffer.write(f"<{tag}")
            for attr, value in attrs.items():
                self._buffer.write(f" {attr}='{value}'")
            self._buffer.write(">")
            self._indent += 1
            self.nl()
            yield
        finally:
            self._indent -= 1
            self.nl()
            if close:
                self._buffer.write(f"</{tag}>")

    @staticmethod
    def _strip_attrs(attrs):
        if "cls" in attrs:
            attrs["class"] = attrs.pop("cls")
        return attrs

    def __str__(self):
        return self._buffer.getvalue()


def construct_preview(meta):
    html = SimpleHTMLConstructor()
    with html.tag("div", cls="row"):
        with html.tag("div", cls="col-3"):
            html.ctx("img", close=False, src=meta["image"], alt=meta.get("title"))
        with html.tag("div", cls="col-9"):
            if meta.get("title"):
                with html.tag("h3"):
                    html.write(meta["title"], " ", meta.get("site_name"))
                    html.ctx("br", close=False)
            if meta.get("description"):
                with html.tag("p"):
                    html.write(meta["description"])

    return html


@register.simple_tag
def get_preview(url):
    parser = MetaParser()
    with urlopen(url) as conn:
        headers = conn.info()
        parser.feed(conn.read().decode())

    return construct_preview(parser._meta)
