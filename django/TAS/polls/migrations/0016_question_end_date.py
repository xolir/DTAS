# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20171111_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ending date'),
            preserve_default=False,
        ),
    ]
