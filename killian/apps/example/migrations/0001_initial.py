# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 09:25
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('date_created', models.DateTimeField(
                    auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(
                    auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'Example',
                'verbose_name_plural': 'Examples',
            },
        ),
    ]
