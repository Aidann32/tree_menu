from django import template
from django.core.exceptions import ObjectDoesNotExist

from apps.menu.models import Menu, MenuItem
from .helpers import build_tree, traverse_tree, get_absolute_url as get_absolute_url_helper


register = template.Library()

@register.inclusion_tag("partials/_menu.html")
def draw_menu(menu_slug: str, request) -> dict:
    items = Menu.objects.filter(slug=menu_slug).values('menu_items__pk', 'menu_items__url', 'menu_items__parent', 'menu_items__name', 'menu_items__children')
    tree = build_tree(items)
    if not items:
        raise ObjectDoesNotExist(f"Menu with slug {menu_slug} does not exists")
    return {'menu_slug': menu_slug, 'items': tree, 'current_url': request.build_absolute_uri() }

@register.inclusion_tag("partials/_submenu.html")
def draw_submenu(items: dict, current_url: str, menu_item_pk: int) -> dict:
    return {'items': items, 'current_url': current_url, 'menu_item_pk': int}

@register.filter
def is_have_active(menu_items: dict, current_url: str) -> bool:
    return traverse_tree(menu_items, current_url)

@register.filter
def get_absolute_url(url: str, current_url: str) -> str:
    return get_absolute_url_helper(url, current_url)
