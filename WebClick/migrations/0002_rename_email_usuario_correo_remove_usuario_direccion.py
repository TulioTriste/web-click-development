# Generated by Django 5.0.6 on 2024-06-26 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebClick', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
    ]
