# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]
