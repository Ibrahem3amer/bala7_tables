# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_auto_20161023_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_section_day',
            name='subject',
            field=models.CharField(max_length=500),
        ),
    ]
