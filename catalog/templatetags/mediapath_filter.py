from django import template


register = template.Library()

@register.filter(needs_autoescape=True)
def mediapath(address, autoescape=True):

    result = "/media/" + str(address)
    return result