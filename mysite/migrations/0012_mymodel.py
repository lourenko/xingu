# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20160522_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_access_maqflux', 'Máquinas de fluxo permission description'), ('can_access_mecflu2', 'Mec. dos Fluidos2 permission description'), ('can_access_sistem3', 'Sistemas Térmicos permission description')),
            },
        ),
    ]
