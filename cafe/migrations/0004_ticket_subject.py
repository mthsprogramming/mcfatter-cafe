# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_auto_20170505_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='subject',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
