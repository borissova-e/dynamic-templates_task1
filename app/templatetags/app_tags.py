from django import template

register = template.Library()


@register.filter()
def inflation_color(value):
    try:
        value = float(value)
        if value < 0:
            color = 'green'
        elif 1 <= value < 2:
            color = 'lightsalmon'
        elif 2 <= value < 5:
            color = 'indianred'
        elif value > 5:
            color = 'red'
        else:
            color = ''
    except ValueError:
        color = ''
    return color
