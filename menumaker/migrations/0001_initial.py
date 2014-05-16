# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table(u'menumaker_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dinner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dinner', to=orm['recipemanager.Recipe'])),
            ('supper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='supper', to=orm['recipemanager.Recipe'])),
        ))
        db.send_create_signal(u'menumaker', ['Day'])

        # Adding model 'Week'
        db.create_table(u'menumaker_week', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'menumaker', ['Week'])

        # Adding M2M table for field days on 'Week'
        m2m_table_name = db.shorten_name(u'menumaker_week_days')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week', models.ForeignKey(orm[u'menumaker.week'], null=False)),
            ('day', models.ForeignKey(orm[u'menumaker.day'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week_id', 'day_id'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table(u'menumaker_day')

        # Deleting model 'Week'
        db.delete_table(u'menumaker_week')

        # Removing M2M table for field days on 'Week'
        db.delete_table(db.shorten_name(u'menumaker_week_days'))


    models = {
        u'menumaker.day': {
            'Meta': {'object_name': 'Day'},
            'dinner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dinner'", 'to': u"orm['recipemanager.Recipe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'supper'", 'to': u"orm['recipemanager.Recipe']"})
        },
        u'menumaker.week': {
            'Meta': {'object_name': 'Week'},
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['menumaker.Day']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'recipemanager.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cook_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'portion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prepare_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['menumaker']