# Generated by Django 4.0.3 on 2024-11-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0021_flight_arrival_time_flight_departure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(null=True),
        ),
    ]
