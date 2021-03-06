# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('ParentCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DAGR.Category')),
            ],
        ),
        migrations.CreateModel(
            name='DAGR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('Author', models.CharField(max_length=50, verbose_name='Author')),
                ('CreationTime', models.DateTimeField(verbose_name='Creation Time')),
                ('LastModified', models.DateTimeField(blank=True, null=True, verbose_name='Last Modified')),
                ('DeletionTime', models.DateTimeField(blank=True, null=True, verbose_name='Deletion Time')),
                ('HasKids', models.BooleanField(verbose_name='Has Kids')),
                ('Size', models.IntegerField(verbose_name='Size')),
                ('CategoryID', models.ManyToManyField(blank=True, to='DAGR.Category')),
                ('Kids', models.ManyToManyField(blank=True, to='DAGR.DAGR')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('Author', models.CharField(max_length=50, verbose_name='Author')),
                ('Size', models.IntegerField(verbose_name='Size')),
                ('Links', models.FileField(upload_to='files/')),
                ('FileName', models.CharField(max_length=50, unique=True, verbose_name='File Name')),
                ('Type', models.CharField(max_length=50, verbose_name='Type')),
                ('Description', models.CharField(max_length=100, verbose_name='Description')),
                ('Owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DAGR.DAGR')),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('Type', models.CharField(max_length=50, verbose_name='Type')),
                ('Description', models.CharField(max_length=100, verbose_name='Description')),
                ('Link', models.CharField(max_length=200, verbose_name='Link')),
                ('Owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DAGR.DAGR')),
            ],
        ),
    ]
