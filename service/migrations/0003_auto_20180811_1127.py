# Generated by Django 2.0.4 on 2018-08-11 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180811_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 11, 5, 57, 1, 570203, tzinfo=utc), verbose_name='date added'),
        ),
    ]
