from django.template.defaulttags import register


@register.filter
def minus(value, arg):
    try:
        return int(float(value)) - int(float(arg))
    except (ValueError, ZeroDivisionError):
        return "-- --"
