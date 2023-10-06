from django import template
from core.models import MenuItem
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    """Показ основного меню на главной странице или любой другой."""
    menu_items = MenuItem.objects.filter(level=1).select_related('parent')
    return {
        'menu_items': menu_items,
    }


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Показ определённого подпункта меню, использовать только меню первой ступени."""
    try:
        menu_items = MenuItem.objects.filter(name=menu_name, level=1).select_related('parent')
        return {
            'menu_items': menu_items,
        }
    except MenuItem.DoesNotExist:
        return {}
