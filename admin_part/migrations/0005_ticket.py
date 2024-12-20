# Generated by Django 5.1 on 2024-10-08 07:28

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0004_passenger'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=6, unique=True)),
                ('flight_ddate', models.DateField(blank=True, null=True)),
                ('flight_adate', models.DateField(blank=True, null=True)),
                ('flight_fare', models.FloatField(blank=True, null=True)),
                ('other_charges', models.FloatField(blank=True, null=True)),
                ('total_fare', models.FloatField(blank=True, null=True)),
                ('seat_class', models.CharField(choices=[('economy', 'Economy'), ('business', 'Business'), ('first', 'First')], max_length=20)),
                ('booking_date', models.DateTimeField(default=datetime.datetime.now)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=45)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], max_length=45)),
                ('flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='admin_part.flight')),
                ('passengers', models.ManyToManyField(related_name='flight_tickets', to='admin_part.passenger')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
