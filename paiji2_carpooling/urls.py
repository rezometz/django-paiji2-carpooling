from django.conf.urls import patterns, url
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
        name="cov-list",
    ),
    url(
        r'add$',
        login_required(CarpoolCreateView.as_view()),
        name="cov-add",
    ),
    url(
        r'edit/(?P<pk>[0-9]+)/$',
        login_required(CarpoolEditView.as_view()),
        name="cov-edit",
    ),
    url(
        r'delete/(?P<pk>[0-9]+)/$',
        login_required(CarpoolDeleteView.as_view()),
        name="cov-delete",
    ),
]
