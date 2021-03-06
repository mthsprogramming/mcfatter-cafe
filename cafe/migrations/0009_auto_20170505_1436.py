# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_auto_20170505_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='carbs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='cholesterol',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='dietary_fiber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='fat',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/cafe/menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='potassium',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='protein',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='sat_fat',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='short_description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='sodium',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='sugar',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='trans_fat',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
