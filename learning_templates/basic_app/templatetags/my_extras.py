from django import template

register = template.Library()

@register.fiter(name='cut')
def cut(value,arg):
    """
    this cuts out alkl values of arg from the string !
    """

    return value.replace(arg,'')

#register.filter('cut',cut)