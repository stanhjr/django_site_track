# Generated by Django 4.0.4 on 2022-08-30 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0014_alter_saleads_sale_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='subscribe_until_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='sale_end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
