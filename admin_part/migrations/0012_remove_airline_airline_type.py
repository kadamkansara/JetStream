# Generated by Django 4.2.16 on 2024-10-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0011_flight_economy_class_price_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='airline_type',
        ),
    ]
