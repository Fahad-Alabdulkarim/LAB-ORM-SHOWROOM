# Generated by Django 5.1.3 on 2024-11-21 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_rename_founded_at_brand_model_made'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='model_made',
            new_name='founded_at',
        ),
    ]
