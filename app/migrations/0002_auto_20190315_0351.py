# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-15 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='phone',
        ),
    ]
