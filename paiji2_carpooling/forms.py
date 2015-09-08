from django.forms import ModelForm
from .models import Carpool
from django.contrib.admin import widgets


class CarpoolForm(ModelForm):
    class Meta:
        model = Carpool
        fields = [
            'annonce_type',
            'good_until',
            'notes',
        ]
        widgets = {
            'good_until': widgets.AdminSplitDateTime()
        }
