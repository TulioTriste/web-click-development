# Generated by Django 5.0 on 2024-07-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebClick', '0007_remove_compra_producto_remove_compra_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates_product',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
        ),
    ]