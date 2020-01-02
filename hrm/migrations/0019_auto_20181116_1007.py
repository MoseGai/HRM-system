# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 10:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrm', '0018_auto_20181116_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='发放日期')),
                ('salary', models.FloatField(default=0, verbose_name='总薪资')),
            ],
            options={
                'verbose_name': '员工薪资管理',
                'verbose_name_plural': '员工薪资管理',
                'db_table': 'salary',
            },
        ),
        migrations.RemoveField(
            model_name='staff',
            name='salary',
        ),
        migrations.AlterModelTable(
            name='attendance',
            table='attendance_message',
        ),
        migrations.AddField(
            model_name='salary',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm.Staff', verbose_name='员工'),
        ),
        migrations.AddField(
            model_name='salary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
