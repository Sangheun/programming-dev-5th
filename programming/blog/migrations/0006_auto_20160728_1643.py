# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-28 07:43
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160728_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator])),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Markdown 문법을 써 주세요.', validators=[blog.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[blog.validators.MinLengthValidator(4)], verbose_name='제목'),
        ),
    ]
