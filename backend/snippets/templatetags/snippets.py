from django import template

from ..models import PhoneNumber

register = template.Library()


@register.inclusion_tag('snippets/phone_numbers.html', takes_context=True)
def get_phone_numbers(context):
    return {
        'phone_numbers': PhoneNumber.objects.all(),
        'request': context['request'],
    }
