# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DAGR', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dagr',
            name='DeletionTime',
            field=models.DateTimeField(blank=True, verbose_name='Deletion Time'),
        ),
        migrations.AlterField(
            model_name='dagr',
            name='LastModified',
            field=models.DateTimeField(blank=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='document',
            name='LastModified',
            field=models.DateTimeField(blank=True, verbose_name='Last Modified'),
        ),
    ]
