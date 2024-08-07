# Generated by Django 5.0.6 on 2024-07-05 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebClick', '0005_alter_templates_product_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebClick.templates_product')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebClick.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebClick.templates_product')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebClick.usuario')),
            ],
        ),
    ]
