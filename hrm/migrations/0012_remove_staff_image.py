# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 19:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0011_auto_20170706_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='image',
        ),
    ]
