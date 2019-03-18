# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-15 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]