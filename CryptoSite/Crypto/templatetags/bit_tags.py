from django import template

from Crypto import views
from Crypto.utils import menu

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('bit/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {"cats": cats, "cat_selected": cat_selected}

@register.simple_tag
def get_menu():
    return menu