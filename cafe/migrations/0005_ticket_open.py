# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_ticket_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]
