# Generated by Django 4.0.3 on 2022-03-26 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_car_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_type',
            old_name='cartype',
            new_name='name',
        ),
    ]
