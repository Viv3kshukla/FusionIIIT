# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_attendance',
            name='current_attend',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='total_attend',
            field=models.IntegerField(default=0),
        ),
    ]
