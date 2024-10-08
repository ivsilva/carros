# Generated by Django 5.0.6 on 2024-08-14 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/photos/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cars.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='cars/videos/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='cars.car')),
            ],
        ),
    ]
