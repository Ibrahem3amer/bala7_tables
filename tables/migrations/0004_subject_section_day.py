# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20161023_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_section_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Subject')),
            ],
        ),
    ]