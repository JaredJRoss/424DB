# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0010_auto_20170504_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dagrcategory',
            old_name='Cat',
            new_name='CategoryID',
        ),
        migrations.RenameField(
            model_name='dagrcategory',
            old_name='DA',
            new_name='DAGRID',
        ),
    ]