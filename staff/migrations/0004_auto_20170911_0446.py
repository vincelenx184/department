# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_remove_employeedetail_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='id_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
