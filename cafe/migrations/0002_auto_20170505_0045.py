# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 04:45
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_text',
            field=tinymce.models.HTMLField(max_length=10000),
        ),
    ]
