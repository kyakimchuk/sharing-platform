# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0011_remove_call_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='call',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Call',
        ),
    ]
