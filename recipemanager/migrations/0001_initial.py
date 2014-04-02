# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuantityType'
        db.create_table(u'recipemanager_quantitytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'recipemanager', ['QuantityType'])

        # Adding model 'Recipe'
        db.create_table(u'recipemanager_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('prepare_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cook_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('portion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'recipemanager', ['Recipe'])

        # Adding model 'Ingredient'
        db.create_table(u'recipemanager_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('seller', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'recipemanager', ['Ingredient'])

        # Adding model 'RecipeIngredient'
        db.create_table(u'recipemanager_recipeingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemanager.Recipe'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemanager.Ingredient'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemanager.QuantityType'])),
        ))
        db.send_create_signal(u'recipemanager', ['RecipeIngredient'])

        # Adding model 'Step'
        db.create_table(u'recipemanager_step', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemanager.Recipe'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'recipemanager', ['Step'])


    def backwards(self, orm):
        # Deleting model 'QuantityType'
        db.delete_table(u'recipemanager_quantitytype')

        # Deleting model 'Recipe'
        db.delete_table(u'recipemanager_recipe')

        # Deleting model 'Ingredient'
        db.delete_table(u'recipemanager_ingredient')

        # Deleting model 'RecipeIngredient'
        db.delete_table(u'recipemanager_recipeingredient')

        # Deleting model 'Step'
        db.delete_table(u'recipemanager_step')


    models = {
        u'recipemanager.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'seller': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipemanager.quantitytype': {
            'Meta': {'object_name': 'QuantityType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        },
        u'recipemanager.recipeingredient': {
            'Meta': {'object_name': 'RecipeIngredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipemanager.Ingredient']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'quantity_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipemanager.QuantityType']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipemanager.Recipe']"})
        },
        u'recipemanager.step': {
            'Meta': {'object_name': 'Step'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipemanager.Recipe']"})
        }
    }

    complete_apps = ['recipemanager']