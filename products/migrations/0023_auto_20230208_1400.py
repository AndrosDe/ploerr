# Generated by Django 3.2 on 2023-02-08 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0022_auto_20230208_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productreview', to='products.product'),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userreviews', to=settings.AUTH_USER_MODEL),
        ),
    ]