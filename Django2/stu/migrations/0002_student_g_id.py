# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='g_id',
            field=models.IntegerField(null=True),
        ),
    ]