# Generated by Django 4.0.4 on 2022-06-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0033_alter_saleads_vehicle_price_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settingsindexhome',
            old_name='our_features_listing_text',
            new_name='part_features_text',
        ),
        migrations.RenameField(
            model_name='settingsindexhome',
            old_name='our_features_listing_title',
            new_name='part_features_title',
        ),
        migrations.RenameField(
            model_name='settingsindexhome',
            old_name='find_top_categories_title',
            new_name='part_start_title',
        ),
        migrations.RenameField(
            model_name='settingsindexhome',
            old_name='find_top_categories_text',
            new_name='part_text_text',
        ),
        migrations.AlterField(
            model_name='saleads',
            name='description',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='others',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]
