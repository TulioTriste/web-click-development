# Generated by Django 5.0.6 on 2024-07-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebClick', '0004_rename_templates_products_templates_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates_product',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
    ]