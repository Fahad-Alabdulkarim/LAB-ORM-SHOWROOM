# Generated by Django 5.0.7 on 2024-07-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='poster',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]