# Generated by Django 5.0.7 on 2024-07-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(to='games.category'),
        ),
    ]