# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-26 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0016_ingestevent'),
        ('recipe', '0034_recipe_configuration'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingest_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ingest.IngestEvent'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trigger.TriggerEvent'),
        ),
    ]
