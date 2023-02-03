# Generated by Django 3.2 on 2023-02-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230201_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='containers', to='products.container'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.product'),
        ),
    ]