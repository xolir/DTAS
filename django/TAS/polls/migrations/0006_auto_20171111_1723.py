# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20171111_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='question',
        ),
        migrations.AddField(
            model_name='user',
            name='question',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]
