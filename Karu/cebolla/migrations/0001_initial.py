# Generated by Django 2.0.5 on 2019-02-19 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField()),
                ('scale', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('itemPrice', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='cebolla.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderPrice', models.IntegerField(default=0)),
                ('rfID', models.IntegerField()),
                ('ongoing', models.BooleanField(default=False)),
                ('receiving', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentTypeName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('totalPrice', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cebolla.Purchase'),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='cebolla.Order'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredientType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cebolla.IngredientType'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('order', 'ingredient')},
        ),
    ]
