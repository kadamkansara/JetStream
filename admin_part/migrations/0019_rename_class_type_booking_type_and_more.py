# Generated by Django 4.2.16 on 2024-11-04 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0018_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='class_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_reference',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='special_requests',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
    ]
