# Generated by Django 4.2.16 on 2024-10-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0015_delete_file_remove_ticket_flight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='estimated_arrival',
            field=models.DateField(null=True),
        ),
    ]