# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_group_slack_webhook'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='another_description',
            field=models.TextField(blank=True),
        ),
    ]
