# custom_filters.py
from django import template
register = template.Library()

@register.filter
def get_texture_by_code(product, texture_code):
    try:
        return product.textures.get(code=texture_code)
    except product.textures.model.DoesNotExist:
        return None
