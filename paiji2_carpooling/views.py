from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.utils.translation import ugettext as _
from django.contrib import messages

from paiji2_carpooling.models import (
    Carpool,
)


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


class CarpoolCreateView(generic.CreateView):
    model = Carpool
    template_name = 'carpooling/carpool/form.html'
    fields = (
        'annonce_type',
        'good_until',
        'notes',
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CarpoolCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request,
            _('Your request has been saved successfully :P')
        )
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')


class CarpoolEditView(CarpoolOwnerMixin, generic.UpdateView):
    model = Carpool
    template_name = 'carpooling/carpool/form.html'
    fields = (
        'annonce_type',
        'good_until',
        'notes',
    )
    message_update = _(
        'Your carpool has been updated, it will be refreshed in a moment'
    )

    def get_success_url(self):
        messages.success(self.request, self.message_update)
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')


class CarpoolDeleteView(CarpoolOwnerMixin, generic.DeleteView):
    model = Carpool
    template_name = 'carpooling/carpool/confirm_delete.html'
    message_delete = _(
        'Your carpool has been removed, it will be refreshed in a moment'
    )

    def get_success_url(self):
        messages.success(self.request, self.message_delete)
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')
