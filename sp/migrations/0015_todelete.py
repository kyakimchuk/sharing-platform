# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0014_auto_20170330_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='todelete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
        ),
    ]