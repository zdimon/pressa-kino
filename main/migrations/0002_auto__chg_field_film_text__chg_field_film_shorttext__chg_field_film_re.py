# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Film.text'
        db.alter_column(u'main_film', 'text', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Film.shorttext'
        db.alter_column(u'main_film', 'shorttext', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Film.release_date'
        db.alter_column(u'main_film', 'release_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Film.image'
        db.alter_column(u'main_film', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Blog.text'
        db.alter_column(u'main_blog', 'text', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Blog.shorttext'
        db.alter_column(u'main_blog', 'shorttext', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Blog.image'
        db.alter_column(u'main_blog', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Festival.text'
        db.alter_column(u'main_festival', 'text', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Festival.image'
        db.alter_column(u'main_festival', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Page.text'
        db.alter_column(u'main_page', 'text', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Page.image'
        db.alter_column(u'main_page', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Film.text'
        db.alter_column(u'main_film', 'text', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Film.shorttext'
        db.alter_column(u'main_film', 'shorttext', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Film.release_date'
        db.alter_column(u'main_film', 'release_date', self.gf('django.db.models.fields.DateField')(default=0))

        # Changing field 'Film.image'
        db.alter_column(u'main_film', 'image', self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100))

        # Changing field 'Blog.text'
        db.alter_column(u'main_blog', 'text', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Blog.shorttext'
        db.alter_column(u'main_blog', 'shorttext', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Blog.image'
        db.alter_column(u'main_blog', 'image', self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100))

        # Changing field 'Festival.text'
        db.alter_column(u'main_festival', 'text', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Festival.image'
        db.alter_column(u'main_festival', 'image', self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100))

        # Changing field 'Page.text'
        db.alter_column(u'main_page', 'text', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Page.image'
        db.alter_column(u'main_page', 'image', self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100))

    models = {
        u'main.blog': {
            'Meta': {'object_name': 'Blog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'shorttext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'main.festival': {
            'Meta': {'object_name': 'Festival'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.film': {
            'Meta': {'object_name': 'Film'},
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
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['main']