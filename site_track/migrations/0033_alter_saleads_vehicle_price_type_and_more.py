# Generated by Django 4.0.4 on 2022-06-21 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0032_remove_saleads_facebook_remove_saleads_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_price_type',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_ads', to='site_track.categoriestrack'),
        ),
    ]
