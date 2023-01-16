# Generated by Django 4.1.4 on 2023-01-16 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_alter_choosecars_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carModels', models.CharField(blank=True, max_length=35, null=True)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_model', to='card.choosecars')),
            ],
        ),
    ]
