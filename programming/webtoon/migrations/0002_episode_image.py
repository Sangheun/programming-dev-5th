# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-14 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
