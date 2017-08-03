#!/usr/bin/env python3
from django.template import Library
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

from markdown import markdown

register = Library()


@register.filter(name="markdown")
@stringfilter
def markdown_format(value):
    return mark_safe(markdown(value, ['extra', 'codehilite', 'toc']))