# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='users_like',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
