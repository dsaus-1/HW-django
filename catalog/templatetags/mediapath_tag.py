from django import template

register = template.Library()

@register.simple_tag
def mediapath(address):
    return "/media/" + str(address)