# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Videos.image'
        db.add_column(u'main_videos', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Videos.image'
        db.delete_column(u'main_videos', 'image')


    models = {
        u'main.blog': {
            'Meta': {'object_name': 'Blog'},
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'shorttext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'main.festival': {
            'Meta': {'object_name': 'Festival'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.film': {
            'Meta': {'object_name': 'Film'},
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'festival': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Festival']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shorttext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.videos': {
            'Meta': {'object_name': 'Videos'},
            'code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Film']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']