# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0024_auto_20170421_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='card',
            field=models.ImageField(blank=True, default='sp/cards/no.png', upload_to='sp/cards', verbose_name='Изображение'),
        ),
    ]
