# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0019_order_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='specials',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cafe.Menu'),
        ),
    ]
