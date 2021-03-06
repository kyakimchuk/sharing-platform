# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 15:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sp', '0007_auto_20170324_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField(choices=[(True, 'Предлагаю'), (False, 'Ищу')], default=False)),
                ('city', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('card', models.ImageField(blank=True, upload_to='sp/cards')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
