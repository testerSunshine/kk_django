# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20181128_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxofficeday',
            name='offer_video_percent',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x8e\x92\xe7\x89\x87\xe5\x8d\xa0\xe6\xaf\x94'),
        ),
    ]
