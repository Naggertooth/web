# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-03 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_tip_txid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='receive_txid',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tip',
            name='received_on',
            field=models.DateTimeField(null=True),
        ),
    ]
