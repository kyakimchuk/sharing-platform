# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 07:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0021_auto_20170406_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Список ключевых слов, взятых в кавычки, через запятую', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='e_mail',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Введите правильный e-mail', regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')], verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=30, verbose_name='Пол'),
        ),
    ]
