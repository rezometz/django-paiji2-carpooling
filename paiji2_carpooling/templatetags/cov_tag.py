from django import template
from django.utils import timezone

from paiji2_carpooling.models import (
    Carpool,
)


register = template.Library()


@register.inclusion_tag('carpooling/carpool/block.html', takes_context=True)
def get_cov(context):
    context['cov'] = Carpool.objects.select_related('author').filter(
        good_until__gte=timezone.now()
    ).order_by('good_until')

    return context
