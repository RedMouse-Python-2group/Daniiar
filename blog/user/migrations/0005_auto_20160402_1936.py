# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 13:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20160402_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=user.models.upload_location_author, width_field='width_field'),
        ),
    ]
