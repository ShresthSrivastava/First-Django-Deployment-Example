from django import template

register = template.library

@register.filter(name="cut")
def cut(value,arg):
    """ Cuts all values 'arg' from string"""

    return value.replace(arg,'')


# register.filter('cut',cut)