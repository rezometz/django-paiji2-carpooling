from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.utils.translation import ugettext as _

from paiji2_carpooling.models import (
    Carpool,
)
from paiji2_utils.views import SuccessUrlMixin


class MySuccessUrl(SuccessUrlMixin):

    default_url_name = 'carpool-list'

    def get_forbidden_urls(self):
        if hasattr(self, 'object'):
            return (
                reverse('carpool-edit', args=[self.object.pk]),
                reverse('carpool-delete', args=[self.object.pk]),
            )
        else:
            return None


class CarpoolOwnerMixin(object):

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update Carpools """
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseNotFound(
                _('Rezo is not hacked. You don\'t have the permission xD')
            )
        return super(CarpoolOwnerMixin, self).dispatch(
            request, *args, **kwargs
        )


class CarpoolListView(generic.ListView):

    model = Carpool
    paginate_by = 10
    context_object_name = 'covs'
    template_name = 'carpooling/carpool/list.html'

    def get_queryset(self):
        return super(CarpoolListView, self).get_queryset().select_related(
            'author'
        )


class CarpoolCreateView(MySuccessUrl, generic.CreateView):

    model = Carpool
    template_name = 'carpooling/carpool/form.html'
    fields = (
        'annonce_type',
        'good_until',
        'notes',
    )
    message_succes = _('Your request has been saved successfully :P')
    forbidden_url_names = (
        'carpool-create',
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CarpoolCreateView, self).form_valid(form)


class CarpoolEditView(CarpoolOwnerMixin,
                      MySuccessUrl,
                      generic.UpdateView):

    model = Carpool
    template_name = 'carpooling/carpool/form.html'
    fields = (
        'annonce_type',
        'good_until',
        'notes',
    )
    message_success = _(
        'Your carpool has been updated, it will be refreshed in a moment'
    )


class CarpoolDeleteView(CarpoolOwnerMixin, MySuccessUrl, generic.DeleteView):
    model = Carpool
    template_name = 'carpooling/carpool/confirm_delete.html'
    message_success = _(
        'Your carpool has been removed, it will be refreshed in a moment'
    )
