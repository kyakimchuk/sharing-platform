# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0019_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='e_mail',
            field=models.CharField(max_length=30, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=30, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Не указано', 'Не указано'), ('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=30, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='offers',
            field=models.TextField(blank=True, verbose_name='Предложения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='search',
            field=models.TextField(blank=True, verbose_name='Поиск'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vk_com',
            field=models.CharField(blank=True, max_length=30, verbose_name='vk.com'),
        ),
    ]
