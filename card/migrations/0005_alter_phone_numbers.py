# Generated by Django 4.1.4 on 2023-01-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_car_car_number_alter_card_main_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='numbers',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
