# Generated by Django 3.2.3 on 2021-07-09 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210709_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boarding',
            old_name='pet',
            new_name='pets',
        ),
    ]