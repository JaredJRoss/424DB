# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0008_auto_20170504_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='ParentCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DAGR.Category'),
        ),
    ]