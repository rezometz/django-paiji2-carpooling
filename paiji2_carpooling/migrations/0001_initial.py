# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carpool'
        db.create_table(u'paiji2_carpooling_carpool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('poster_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('annonce_type', self.gf('django.db.models.fields.IntegerField')()),
            ('itinerary', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('n_places', self.gf('django.db.models.fields.IntegerField')()),
            ('dept_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('ret_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'paiji2_carpooling', ['Carpool'])


    def backwards(self, orm):
        # Deleting model 'Carpool'
        db.delete_table(u'paiji2_carpooling_carpool')


    models = {
        u'paiji2_carpooling.carpool': {
            'Meta': {'object_name': 'Carpool'},
            'annonce_type': ('django.db.models.fields.IntegerField', [], {}),
            'dept_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itinerary': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'n_places': ('django.db.models.fields.IntegerField', [], {}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'poster_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'ret_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['paiji2_carpooling']
