# Generated by Django 4.0.4 on 2023-01-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0020_tiresize_alter_saleads_tire_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleads',
            name='body_damage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
