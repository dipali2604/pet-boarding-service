# Generated by Django 3.2.3 on 2021-07-09 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210709_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boarding',
            old_name='pets',
            new_name='pet',
        ),
    ]
