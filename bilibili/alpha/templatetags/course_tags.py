from django import template
from alpha.models import CourseCategory

register = template.Library()

@register.simple_tag
def render_node(node):
    children = node.get_children()
    return {'node': node, 'children': children}
