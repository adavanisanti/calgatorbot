# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_venue_venueid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='zipcode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
