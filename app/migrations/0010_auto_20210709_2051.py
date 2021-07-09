# Generated by Django 3.2.3 on 2021-07-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_boarding_pick_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarding',
            name='is_payment_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='boarding',
            name='status',
            field=models.CharField(choices=[('requested', 'requested'), ('Preparing', 'preparing'), ('Pickup', 'pickup'), ('delivered', 'delivered'), ('Boarded', 'boarded'), ('on the way', 'on the way')], default='requested', max_length=20),
        ),
    ]
