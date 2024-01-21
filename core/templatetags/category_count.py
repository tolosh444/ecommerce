from django import template

register = template.Library()

@register.filter
def get_category_count(category_counts, category_id):
    return category_counts.get(category_id, 0)