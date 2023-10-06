from django.db.models.query import QuerySet
from django.urls.exceptions import NoReverseMatch
from django.urls import reverse

from urllib.parse import urlparse


def build_tree(data: QuerySet, parent=None) -> dict:
    tree = {}
    for item in data:
        if item['menu_items__parent'] == parent:
            children = build_tree(data, item['menu_items__pk'])
            if children:
                item['menu_items__children'] = children
            tree[item['menu_items__pk']] = item
    return tree

def get_absolute_url(url: str, current_url: str) -> str:
    if not url:
        return '#'
    if 'named_url:' in url:
        url_name = url.replace('named_url:', '')
        host_name = urlparse(current_url).netloc
        try:
            return f'http://{host_name}{reverse(url_name)}'
        except NoReverseMatch:
            return '#'
    return url

def traverse_tree(tree: dict, current_url: str, level=0):
    for key, node in tree.items():
        if get_absolute_url(node['menu_items__url'], current_url) == current_url:
            return True 
        if node["menu_items__children"]:
            traverse_tree(node["menu_items__children"], current_url, level + 1)
        return False 