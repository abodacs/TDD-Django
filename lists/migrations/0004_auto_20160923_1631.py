# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20160923_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
