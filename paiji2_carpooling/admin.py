from django.contrib import admin

from paiji2_carpooling.models import (
    Covoiturage as Carpool,
)


class CarpoolAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'annonce_type',
        'good_until',
        'notes',
        'posted_at',
    )


admin.site.register(Carpool, CarpoolAdmin)
