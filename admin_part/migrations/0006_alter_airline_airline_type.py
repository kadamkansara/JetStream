# Generated by Django 5.1 on 2024-10-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0005_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='airline_type',
            field=models.CharField(choices=[('economy', 'Economy'), ('business', 'Business'), ('first', 'First')], max_length=100),
        ),
    ]
