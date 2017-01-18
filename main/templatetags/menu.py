from django import template
from main.models import Page
register = template.Library()

@register.simple_tag
def get_menu():
    str = ''
    for i in Page.objects.filter(in_menu=True):
        str += '<a href="/page/%s.html" type="button" class="btn btn-default">%s</a>&nbsp;' % (i.alias, i.title)
    return str
