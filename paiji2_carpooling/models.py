from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import (
    ugettext as _,
    pgettext,
)


try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except:
    from django.conf import settings
    User = settings.AUTH_USER_MODEL


def default_good_until():
    return timezone.now() + timedelta(days=3)


class Carpool(models.Model):
    OFFER = 0
    SEARCH = 1
    ANNONCE_TYPE = (
        (OFFER, pgettext('1st p sg', 'Offer')),
        (SEARCH, pgettext('1st p sg', 'Search')),
    )

    author = models.ForeignKey(
        User,
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
        default=default_good_until,
    )

    posted_at = models.DateTimeField(
        _('publication date'),
    )

    notes = models.CharField(
        _('description'),
        max_length=150,
    )

    def __unicode__(self):
        if self.annonce_type is self.OFFER:
            action = _('offers')
        else:
            action = _('searches')

        return "{author} {action} {notes}".format(
            author=self.author.get_full_name(),
            action=action,
            notes=self.notes,
        )

    def isGood(self):
        return self.good_until > timezone.now()
    isGood.short_description = _('still current ?')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.posted_at = timezone.now()
        super(Carpool, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('carpool')
        verbose_name_plural = _('carpools')
        ordering = ('-posted_at', )
