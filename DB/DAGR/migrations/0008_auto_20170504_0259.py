# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0007_category_dagr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='ParentCategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DAGR.Category'),
        ),
    ]