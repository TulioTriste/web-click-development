# Generated by Django 5.0.6 on 2024-07-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebClick', '0006_carrito_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='templates_product',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
    ]