# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20171111_1901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
