# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0013_group_another_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='another_description',
        ),
    ]