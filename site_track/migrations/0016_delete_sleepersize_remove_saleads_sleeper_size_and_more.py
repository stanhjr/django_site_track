# Generated by Django 4.0.4 on 2023-01-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0015_remove_saleads_sleeper_size_new_saleads_sleeper_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SleeperSize',
        ),
        migrations.RemoveField(
            model_name='saleads',
            name='sleeper_size',
        ),
        migrations.DeleteModel(
            name='SleeperSizeNew',
        ),
    ]
