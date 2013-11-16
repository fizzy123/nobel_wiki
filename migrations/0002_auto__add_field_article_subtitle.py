# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.subtitle'
        db.add_column(u'wiki_article', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.subtitle'
        db.delete_column(u'wiki_article', 'subtitle')


    models = {
        u'wiki.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'default': "'Fill me with content'"}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Index'", 'max_length': '200', 'primary_key': 'True'})
        }
    }

    complete_apps = ['wiki']