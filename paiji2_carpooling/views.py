from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.utils.translation import ugettext as _
from django.contrib import messages

from paiji2_carpooling.models import (
    Carpool,
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


# TODO factorize user authorization
class CarpoolEditView(generic.UpdateView):
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

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update Covs """
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseNotFound(
                _('Rezo is not hacked. You don\'t have the permission xD')
            )
        return super(CarpoolEditView, self).dispatch(
            request, *args, **kwargs
        )

    def get_success_url(self):
        messages.success(self.request, self.message_update)
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')


class CarpoolDeleteView(generic.DeleteView):
    model = Carpool
    template_name = 'carpooling/carpool/confirm_delete.html'
    message_delete = _(
        'Your carpool has been removed, it will be refreshed in a moment'
    )

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update Covs """
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseNotFound(
                _('Rezo is not hacked. You don\'t have the permission xD')
            )
        return super(CarpoolDeleteView, self).dispatch(
            request, *args, **kwargs
        )

    def get_success_url(self):
        messages.success(self.request, self.message_delete)
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')
