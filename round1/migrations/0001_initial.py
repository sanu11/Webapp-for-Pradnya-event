# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jquestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.IntegerField(unique=True)),
                ('question', models.CharField(max_length=1000)),
                ('op1', models.CharField(max_length=1000)),
                ('op2', models.CharField(max_length=1000)),
                ('op3', models.CharField(max_length=1000)),
                ('op4', models.CharField(max_length=1000)),
                ('ans', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Junior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=15)),
                ('user2', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('score', models.IntegerField(default=0)),
                ('logintime', models.IntegerField(default=0)),
                ('timestamp', models.IntegerField(default=1800)),
                ('array', models.CharField(blank=True, max_length=1000, null=True)),
                ('ans_array', models.CharField(blank=True, max_length=1000, null=True)),
                ('flag', models.IntegerField(default=0)),
                ('correct_count', models.IntegerField(default=0)),
                ('percent', models.IntegerField(default=0)),
                ('percent_flag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=15)),
                ('user2', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('score', models.IntegerField(default=0)),
                ('logintime', models.IntegerField(default=0)),
                ('timestamp', models.IntegerField(default=1800)),
                ('array', models.CharField(blank=True, max_length=1000, null=True)),
                ('ans_array', models.CharField(blank=True, max_length=1000, null=True)),
                ('flag', models.IntegerField(default=0)),
                ('correct_count', models.IntegerField(default=0)),
                ('percent', models.IntegerField(default=0)),
                ('percent_flag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='squestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.IntegerField(unique=True)),
                ('question', models.CharField(max_length=1000)),
                ('op1', models.CharField(max_length=1000)),
                ('op2', models.CharField(max_length=1000)),
                ('op3', models.CharField(max_length=1000)),
                ('op4', models.CharField(max_length=1000)),
                ('ans', models.CharField(max_length=5)),
            ],
        ),
    ]
