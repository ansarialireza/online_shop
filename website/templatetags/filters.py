# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='instanceof')
def isinstanceof(value, class_name):
    return value.__class__.__name__ == class_name
