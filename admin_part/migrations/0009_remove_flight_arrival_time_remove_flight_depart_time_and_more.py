# Generated by Django 4.2.16 on 2024-10-19 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0008_place_date_added_place_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='depart_time',
        ),
        migrations.AddField(
            model_name='flight',
            name='air_craft_code',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='flight',
            name='business_class_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='business_class_slots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='code',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='flight',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='delete_flag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='economy_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='economy_slots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='estimated_arrival',
            field=models.DateTimeField(null=True),
        ),
    ]
