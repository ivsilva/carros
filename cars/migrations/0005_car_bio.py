# Generated by Django 5.0.6 on 2024-07-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
