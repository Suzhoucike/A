# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='category_has_children')
def category_has_children(category_id, categories):
    return any(category.parent_id == category_id for category in categories)

@register.filter(name='category_children')
def category_children(category_id, categories):
    return categories.filter(parent_id=category_id)
