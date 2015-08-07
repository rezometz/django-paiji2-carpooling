# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Carpool.n_places'
        db.delete_column(u'paiji2_carpooling_carpool', 'n_places')

        # Deleting field 'Carpool.ret_datetime'
        db.delete_column(u'paiji2_carpooling_carpool', 'ret_datetime')

        # Deleting field 'Carpool.dept_datetime'
        db.delete_column(u'paiji2_carpooling_carpool', 'dept_datetime')

        # Deleting field 'Carpool.price_per_trip'
        db.delete_column(u'paiji2_carpooling_carpool', 'price_per_trip')

        # Deleting field 'Carpool.itinerary'
        db.delete_column(u'paiji2_carpooling_carpool', 'itinerary')

        # Adding field 'Carpool.good_until'
        db.add_column(u'paiji2_carpooling_carpool', 'good_until',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 15, 0, 0)),
                      keep_default=False)


        # Changing field 'Carpool.notes'
        db.alter_column(u'paiji2_carpooling_carpool', 'notes', self.gf('django.db.models.fields.CharField')(max_length=150))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Carpool.n_places'
        raise RuntimeError("Cannot reverse this migration. 'Carpool.n_places' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration        # Adding field 'Carpool.n_places'
        db.add_column(u'paiji2_carpooling_carpool', 'n_places',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Adding field 'Carpool.ret_datetime'
        db.add_column(u'paiji2_carpooling_carpool', 'ret_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Carpool.dept_datetime'
        raise RuntimeError("Cannot reverse this migration. 'Carpool.dept_datetime' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration        # Adding field 'Carpool.dept_datetime'
        db.add_column(u'paiji2_carpooling_carpool', 'dept_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Adding field 'Carpool.price_per_trip'
        db.add_column(u'paiji2_carpooling_carpool', 'price_per_trip',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Carpool.itinerary'
        raise RuntimeError("Cannot reverse this migration. 'Carpool.itinerary' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration        # Adding field 'Carpool.itinerary'
        db.add_column(u'paiji2_carpooling_carpool', 'itinerary',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)

        # Deleting field 'Carpool.good_until'
        db.delete_column(u'paiji2_carpooling_carpool', 'good_until')


        # Changing field 'Carpool.notes'
        db.alter_column(u'paiji2_carpooling_carpool', 'notes', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'paiji2_carpooling.carpool': {
            'Meta': {'object_name': 'Carpool'},
            'annonce_type': ('django.db.models.fields.IntegerField', [], {}),
            'good_until': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 15, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'poster_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['paiji2_carpooling']
