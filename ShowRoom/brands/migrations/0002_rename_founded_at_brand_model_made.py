# Generated by Django 5.1.3 on 2024-11-21 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='founded_at',
            new_name='model_made',
        ),
    ]
