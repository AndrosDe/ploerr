# Generated by Django 3.2 on 2023-02-01 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20230201_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='container',
            old_name='deposit',
            new_name='deposit_per_unit',
        ),
        migrations.RenameField(
            model_name='container',
            old_name='volumen',
            new_name='volumen_per_unit',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='total_deposit',
            new_name='deposit',
        ),
    ]