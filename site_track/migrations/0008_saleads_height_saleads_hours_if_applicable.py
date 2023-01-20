# Generated by Django 4.0.4 on 2023-01-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0007_rename_springride_suspension_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleads',
            name='height',
            field=models.PositiveIntegerField(blank=True, default=1000, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='hours_if_applicable',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
