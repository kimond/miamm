# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'recipetype'
        db.create_table(u'recipemanager_recipetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typename', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'recipemanager', ['recipetype'])

        # Adding model 'unitlist'
        db.create_table(u'recipemanager_unitlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unitname', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'recipemanager', ['unitlist'])

        # Adding model 'ingredient'
        db.create_table(u'recipemanager_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'recipemanager', ['ingredient'])

        # Adding model 'step'
        db.create_table(u'recipemanager_step', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('step_no', self.gf('django.db.models.fields.IntegerField')()),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemanager.ingredient'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemanager.unitlist'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'recipemanager', ['step'])

        # Adding model 'recipe'
        db.create_table(u'recipemanager_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'recipemanager', ['recipe'])

        # Adding M2M table for field steps on 'recipe'
        m2m_table_name = db.shorten_name(u'recipemanager_recipe_steps')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'recipemanager.recipe'], null=False)),
            ('step', models.ForeignKey(orm[u'recipemanager.step'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'step_id'])


    def backwards(self, orm):
        # Deleting model 'recipetype'
        db.delete_table(u'recipemanager_recipetype')

        # Deleting model 'unitlist'
        db.delete_table(u'recipemanager_unitlist')

        # Deleting model 'ingredient'
        db.delete_table(u'recipemanager_ingredient')

        # Deleting model 'step'
        db.delete_table(u'recipemanager_step')

        # Deleting model 'recipe'
        db.delete_table(u'recipemanager_recipe')

        # Removing M2M table for field steps on 'recipe'
        db.delete_table(db.shorten_name(u'recipemanager_recipe_steps'))


    models = {
        u'recipemanager.ingredient': {
            'Meta': {'object_name': 'ingredient'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'recipemanager.recipe': {
            'Meta': {'object_name': 'recipe'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'steps': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipemanager.step']", 'symmetrical': 'False'})
        },
        u'recipemanager.recipetype': {
            'Meta': {'object_name': 'recipetype'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'typename': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'recipemanager.step': {
            'Meta': {'object_name': 'step'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipemanager.ingredient']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'step_no': ('django.db.models.fields.IntegerField', [], {}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipemanager.unitlist']"})
        },
        u'recipemanager.unitlist': {
            'Meta': {'object_name': 'unitlist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unitname': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['recipemanager']