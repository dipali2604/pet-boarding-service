# Generated by Django 3.2.5 on 2021-07-09 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210709_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarding',
            name='pick_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]