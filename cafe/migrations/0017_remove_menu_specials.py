# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 19:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0016_category_used_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='specials',
        ),
    ]