# Generated by Django 4.1.4 on 2022-12-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_remove_card_main_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_main',
            name='family',
            field=models.ManyToManyField(blank=True, to='card.card_main'),
        ),
        migrations.AddField(
            model_name='card_main',
            name='friends',
            field=models.ManyToManyField(blank=True, to='card.card_main'),
        ),
    ]
