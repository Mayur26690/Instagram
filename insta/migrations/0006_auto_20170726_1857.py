# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='insta/static/img/no_image.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
