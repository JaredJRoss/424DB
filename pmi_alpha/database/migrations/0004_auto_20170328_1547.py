# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20170323_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract_employee',
            name='CustomerID',
        ),
        migrations.RemoveField(
            model_name='contract_employee',
            name='VendorID',
        ),
        migrations.RemoveField(
            model_name='customer_employee',
            name='VendorID',
        ),
        migrations.RemoveField(
            model_name='department_employee',
            name='ContractID',
        ),
        migrations.RemoveField(
            model_name='department_employee',
            name='CustomerID',
        ),
        migrations.RemoveField(
            model_name='department_employee',
            name='VendorID',
        ),
        migrations.RemoveField(
            model_name='googlegroup_employee',
            name='VendorID',
        ),
        migrations.RemoveField(
            model_name='vendor_contract',
            name='CustomerID',
        ),
        migrations.AddField(
            model_name='contract',
            name='Employees',
            field=models.ManyToManyField(through='database.Contract_Employee', to='database.Employee'),
        ),
        migrations.AddField(
            model_name='contract',
            name='Vendors',
            field=models.ManyToManyField(through='database.Vendor_Contract', to='database.Vendor'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Employees',
            field=models.ManyToManyField(through='database.Customer_Employee', to='database.Employee'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Partners',
            field=models.ManyToManyField(through='database.Customer_Partner', to='database.Partner'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Vendors',
            field=models.ManyToManyField(through='database.Customer_Vendor', to='database.Vendor'),
        ),
        migrations.AddField(
            model_name='department',
            name='Employees',
            field=models.ManyToManyField(through='database.Department_Employee', to='database.Employee'),
        ),
        migrations.AddField(
            model_name='googlegroup',
            name='Employees',
            field=models.ManyToManyField(through='database.GoogleGroup_Employee', to='database.Employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='FName',
            field=models.CharField(default=None, max_length=20, verbose_name='Resource First Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='LName',
            field=models.CharField(default=None, max_length=20, verbose_name='Resource Last Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='MName',
            field=models.CharField(default=None, max_length=20, verbose_name='Resource Middle Name'),
        ),
        migrations.AlterField(
            model_name='poc',
            name='FName',
            field=models.CharField(max_length=20, verbose_name='Resource First Name'),
        ),
        migrations.AlterField(
            model_name='poc',
            name='LName',
            field=models.CharField(max_length=20, verbose_name='Resource Last Name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='Phone',
            field=models.CharField(default=None, max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='State',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='TIN',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='ZipCode',
            field=models.CharField(default=None, max_length=10, verbose_name='Zip Code'),
        ),
    ]
