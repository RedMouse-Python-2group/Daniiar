# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20160325_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('list', 'list'), ('useful', 'useful'), ('events', 'events'), ('other', 'other')], default='list', max_length=120),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
