# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20171118_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='name',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]