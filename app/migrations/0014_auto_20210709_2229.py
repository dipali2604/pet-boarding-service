# Generated by Django 3.2.3 on 2021-07-09 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_pet_boarding_pets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boarding',
            name='pets',
        ),
        migrations.AddField(
            model_name='boarding',
            name='pets',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='boardings', to='app.pet'),
            preserve_default=False,
        ),
    ]
