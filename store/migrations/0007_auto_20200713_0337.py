# Generated by Django 3.0.6 on 2020-07-13 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200713_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.TimeField(default=datetime.time(3, 37, 2, 295426)),
        ),
    ]
