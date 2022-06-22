# Generated by Django 4.0.4 on 2022-06-22 20:47

from django.db import migrations, models
import site_track.models


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0038_settingsheaderinventorygrid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsHeaderInventoryCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_title', models.TextField(default='Inventory Catalog View')),
                ('inventory_link_name', models.TextField(default='Inventory Catalog')),
            ],
            bases=(models.Model, site_track.models.IsNotSingleHeaderMixin),
        ),
        migrations.DeleteModel(
            name='SettingsHeaderInventoryList',
        ),
    ]
