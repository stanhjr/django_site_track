# Generated by Django 4.0.4 on 2023-01-20 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0010_engine_horsepower_sleepersize_transmission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleads',
            name='sleeper_size',
        ),
    ]