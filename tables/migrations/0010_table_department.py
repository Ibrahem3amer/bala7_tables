# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_auto_20161028_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='table_department', to='tables.Department'),
            preserve_default=False,
        ),
    ]
