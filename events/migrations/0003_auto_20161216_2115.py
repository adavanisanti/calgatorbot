# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20161216_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='feed_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='feed_id'),
        ),
        migrations.AddField(
            model_name='venue',
            name='mapurl',
            field=models.URLField(blank=True, default='', verbose_name='mapurl'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
