# Generated by Django 4.0.3 on 2022-03-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
