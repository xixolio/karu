# Generated by Django 2.0.5 on 2018-12-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cebolla', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cardId',
            new_name='rfID',
        ),
        migrations.AddField(
            model_name='order',
            name='ongoing',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
