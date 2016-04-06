# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20160325_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('news', 'news'), ('useful', 'useful'), ('events', 'events'), ('other', 'other')], default='news', max_length=120),
        ),
    ]