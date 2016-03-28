# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 09:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 3, 21, 9, 15, 30, 718136, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
