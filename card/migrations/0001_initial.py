# Generated by Django 4.1.4 on 2022-12-29 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carModels', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Card_Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=60)),
                ('fathername', models.CharField(max_length=60)),
                ('brith_year', models.IntegerField(blank=True, null=True)),
                ('features', models.TextField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card_main')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_main', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colors', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=35)),
                ('position', models.CharField(blank=True, max_length=60)),
                ('company_address', models.CharField(blank=True, max_length=35)),
                ('card_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='tiktok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(blank=True, max_length=35)),
                ('card_tiktok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiktok', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('user_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField(blank=True)),
                ('ph_numbers_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(blank=True, max_length=35)),
                ('card_instagram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instagram', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(blank=True, max_length=45, null=True)),
                ('card_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(blank=True, max_length=35)),
                ('card_facebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facebook', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(blank=True, max_length=35)),
                ('car_number', models.CharField(blank=True, max_length=7)),
                ('car_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='card.color')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='card.car_model')),
                ('card_cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BooleanField()),
                ('lanme', models.BooleanField()),
                ('father_name', models.BooleanField()),
                ('birth_year', models.BooleanField()),
                ('features', models.BooleanField()),
                ('family', models.BooleanField()),
                ('friends', models.BooleanField()),
                ('facebook', models.BooleanField()),
                ('tiktok', models.BooleanField()),
                ('instagram', models.BooleanField()),
                ('images', models.BooleanField()),
                ('phone', models.BooleanField()),
                ('home', models.BooleanField()),
                ('work', models.BooleanField()),
                ('car', models.BooleanField()),
                ('card_about', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card_main1', to='card.card_main')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('card_comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='card.card_main')),
                ('comments', models.TextField(blank=True, null=True)),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]