# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0005_remove_dagr_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='FileName',
            field=models.CharField(default=2, max_length=50, unique=True, verbose_name='File Name'),
            preserve_default=False,
        ),
    ]