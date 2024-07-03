from django import template

register = template.Library()


@register.filter(name="trim")
def trim(value):
    return value.strip()


@register.filter(name="split_string")
def split_string(value, key):
    return value.split(key)
