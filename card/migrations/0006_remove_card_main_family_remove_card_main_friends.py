# Generated by Django 4.1.4 on 2023-01-07 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_card_main_family_card_main_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card_main',
            name='family',
        ),
        migrations.RemoveField(
            model_name='card_main',
            name='friends',
        ),
    ]