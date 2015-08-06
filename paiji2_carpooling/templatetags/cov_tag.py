from django import template
from django.utils import timezone

from paiji2_carpooling.models import (
    Covoiturage as Carpool,
)


register = template.Library()


@register.inclusion_tag('cov/cov_block.html', takes_context=True)
def get_cov(context):
    context['cov'] = Covoiturage.objects.select_related('author').filter(
        good_until__gte=timezone.now()
    ).order_by('good_until')

    return context
