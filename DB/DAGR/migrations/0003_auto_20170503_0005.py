# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0002_auto_20170503_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DAGR.DAGR'),
        ),
    ]