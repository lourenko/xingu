# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_post_descr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descr',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
