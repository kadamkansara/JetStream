# Generated by Django 5.1 on 2024-09-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_part', '0002_auto_20240904_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
