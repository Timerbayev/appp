# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-07 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='question',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='added_add',
            new_name='added_at',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='added_add',
            new_name='added_at',
        ),
    ]
