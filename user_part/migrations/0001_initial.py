# Generated by Django 4.0.3 on 2024-08-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usertable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_mail', models.EmailField(max_length=254)),
                ('user_password', models.TextField()),
            ],
            options={
                'db_table': 'Usertable',
            },
        ),
    ]
