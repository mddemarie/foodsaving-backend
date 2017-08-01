# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0014_pickupdateseries_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickupdate',
            name='food_weight',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pickupdate',
            name='user_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pickupdate',
            name='user_feedback',
            field=models.CharField(default=True, max_length=600),
        ),
    ]