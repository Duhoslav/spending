from django import template

register = template.Library()


@register.filter
def divide(dividend, divisor):
    try:
        return int(dividend) / int(divisor)
    except (ValueError, ZeroDivisionError):
        return None
