from django.conf.urls import url  # , patterns
from django.contrib.auth.decorators import login_required

from paiji2_carpooling.views import (
   CarpoolListView,
   CarpoolCreateView,
   CarpoolEditView,
   CarpoolDeleteView,
)


urlpatterns = [
    url(
        r'^$',
        login_required(CarpoolListView.as_view()),
        name="carpool-list",
    ),
    url(
        r'add$',
        login_required(CarpoolCreateView.as_view()),
        name="carpool-create",
    ),
    url(
        r'edit/(?P<pk>[0-9]+)/$',
        login_required(CarpoolEditView.as_view()),
        name="carpool-edit",
    ),
    url(
        r'delete/(?P<pk>[0-9]+)/$',
        login_required(CarpoolDeleteView.as_view()),
        name="carpool-delete",
    ),
]
