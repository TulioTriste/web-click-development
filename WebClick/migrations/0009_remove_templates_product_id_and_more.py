# Generated by Django 5.0 on 2024-07-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebClick', '0008_alter_templates_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templates_product',
            name='id',
        ),
        migrations.AlterField(
            model_name='templates_product',
            name='titulo',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, unique=True),
        ),
    ]
