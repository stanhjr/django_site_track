# Generated by Django 4.0.4 on 2022-08-26 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0004_saleads_last_price_saleads_sale_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleads',
            name='sale_end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]