# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cebolla', '0008_auto_20170807_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localuser',
            name='job',
            field=models.CharField(choices=[('A', 'Local Admin'), ('K', 'kitchen'), ('S', 'script'), ('G', 'global')], max_length=1),
        ),
        migrations.AlterField(
            model_name='localuser',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localUsers', to='cebolla.Local'),
        ),
    ]
