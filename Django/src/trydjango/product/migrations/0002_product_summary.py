# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='test text'),
        ),
    ]
