# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170826_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
