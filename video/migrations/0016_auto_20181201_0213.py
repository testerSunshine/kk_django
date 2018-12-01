# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-01 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0015_auto_20181201_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mouth_word',
            old_name='cityName',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='mouth_word',
            old_name='nickName',
            new_name='nick_name',
        ),
        migrations.AddField(
            model_name='mouth_word',
            name='video_release_time',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xe5\xbd\xb1\xe7\x89\x87\xe4\xb8\x8a\xe6\x98\xa0\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]