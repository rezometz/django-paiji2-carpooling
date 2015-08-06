from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import (
    ugettext as _,
    pgettext,
)


class Covoiturage(models.Model):
    OFFER = 0
    SEARCH = 1
    ANNONCE_TYPE = (
        (OFFER, pgettext('1st p sg','Offer')),
        (SEARCH, pgettext('1st p sg','Search')),
    )

    author = models.ForeignKey(
        get_user_model(),
        verbose_name=_('author'),
        related_name='covs',
    )

    annonce_type = models.IntegerField(
        _('advert type'),
        choices=ANNONCE_TYPE,
        blank=False,
    )

    good_until = models.DateTimeField(
        _('advert validity deadline'),
        default = timezone.now()+timedelta(days=3),
    )

    posted_at = models.DateTimeField(
        _('publication date'),
    )

    notes = models.CharField(
        _('description'),
        max_length=150,
    )

    def __unicode__(self):
        return "{author} {action} {notes}".format(
            author=self.author.get_full_name(),
            action=_('offers') if self.ANNONCE_TYPE is self.OFFER else _('searches'),
            notes=self.notes,
        )

    def isGood(self):
        return self.good_until > timezone.now()
    isGood.short_description = _('still current ?')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.posted_at = timezone.now()
        super(Covoiturage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('carpool')
        verbose_name_plural = _('carpools')
        ordering = ('-posted_at', )
