# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20160515_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
