# Generated by Django 3.2 on 2023-02-06 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='user_comment',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='user_rating',
        ),
    ]