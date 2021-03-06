# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cebolla', '0005_auto_20170805_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ingredientLocal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cebolla.IngredientLocal'),
        ),
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cebolla.Order'),
        ),
    ]
