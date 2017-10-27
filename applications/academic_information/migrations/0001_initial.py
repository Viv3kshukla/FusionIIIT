# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Calendar',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=100, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('credits', models.IntegerField()),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Exam_timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('exam_time_table', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Exam_Timetable',
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('grade', models.CharField(max_length=4)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
            options={
                'db_table': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_date', models.DateField()),
                ('holiday_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Holiday',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
            options={
                'db_table': 'Instructor',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('agenda', models.TextField()),
                ('minutes_file', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='Spi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('spi', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'Spi',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globals.ExtraInfo')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('cpi', models.FloatField(default=0)),
                ('category', models.CharField(choices=[('GEN', 'General'), ('SC', 'Scheduled Castes'), ('ST', 'Scheduled Tribes'), ('OBC', 'Other Backward Classes')], max_length=10)),
                ('father_name', models.CharField(default='', max_length=40)),
                ('mother_name', models.CharField(default='', max_length=40)),
                ('hall_no', models.IntegerField(default=1)),
                ('room_no', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend', models.CharField(choices=[('present', 'present'), ('absent', 'absent')], max_length=6)),
                ('date', models.DateField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Student_attendance',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('time_table', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Timetable',
            },
        ),
        migrations.AddField(
            model_name='spi',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='instructor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo'),
        ),
        migrations.AddField(
            model_name='grades',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('course_id', 'course_name', 'sem')]),
        ),
        migrations.AlterUniqueTogether(
            name='spi',
            unique_together=set([('student_id', 'sem')]),
        ),
        migrations.AlterUniqueTogether(
            name='instructor',
            unique_together=set([('course_id', 'instructor_id')]),
        ),
    ]
