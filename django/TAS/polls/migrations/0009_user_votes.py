# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20171111_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
