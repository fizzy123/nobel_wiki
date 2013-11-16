# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'wiki_article', (
            ('title', self.gf('django.db.models.fields.CharField')(default='Index', max_length=200, primary_key=True)),
            ('last_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='Fill me with content')),
        ))
        db.send_create_signal(u'wiki', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'wiki_article')


    models = {
        u'wiki.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'default': "'Fill me with content'"}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Index'", 'max_length': '200', 'primary_key': 'True'})
        }
    }

    complete_apps = ['wiki']