# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import paiji2_carpooling.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annonce_type', models.IntegerField(verbose_name='advert type', choices=[(0, 'Offer'), (1, 'Search')])),
                ('good_until', models.DateTimeField(default=paiji2_carpooling.models.default_good_until, verbose_name='advert validity deadline')),
                ('posted_at', models.DateTimeField(verbose_name='publication date')),
                ('notes', models.CharField(max_length=150, verbose_name='description')),
                ('author', models.ForeignKey(related_name='covs', verbose_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-posted_at',),
                'verbose_name': 'carpool',
                'verbose_name_plural': 'carpools',
            },
        ),
    ]
