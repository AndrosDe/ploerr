# Generated by Django 3.2 on 2023-02-01 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderlineitem_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='item',
            new_name='product_item',
        ),
    ]
