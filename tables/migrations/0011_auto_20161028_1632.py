# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_table_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='day',
            field=models.CharField(max_length=25),
        ),
    ]