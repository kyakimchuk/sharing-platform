# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0026_auto_20170421_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=70, verbose_name='Образование'),
        ),
    ]