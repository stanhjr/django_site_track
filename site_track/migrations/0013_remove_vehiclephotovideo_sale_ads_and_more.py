# Generated by Django 4.0.4 on 2022-06-19 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0012_vehiclephotovideo_linkedin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclephotovideo',
            name='sale_ads',
        ),
        migrations.RemoveField(
            model_name='vendoraddress',
            name='sale_ads',
        ),
        migrations.AddField(
            model_name='saleads',
            name='air_conditioning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='alarm_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='am_fm_radio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='bluetooth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='cd_player',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='city',
            field=models.CharField(default='https://pypi.org/', max_length=120),
        ),
        migrations.AddField(
            model_name='saleads',
            name='country',
            field=models.CharField(default='https://pypi.org/', max_length=120),
        ),
        migrations.AddField(
            model_name='saleads',
            name='cruise_control',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='cylinders',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='driver_air_bag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='email',
            field=models.EmailField(default='fdfdf@mail.ua', max_length=254),
        ),
        migrations.AddField(
            model_name='saleads',
            name='facebook',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='instagram',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='integrated_phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='linkedin',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='others',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='panoramic_roof',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='phone_number',
            field=models.CharField(default='+3809568422', max_length=30),
        ),
        migrations.AddField(
            model_name='saleads',
            name='pinterest',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='post_code',
            field=models.CharField(default='https://pypi.org/', max_length=120),
        ),
        migrations.AddField(
            model_name='saleads',
            name='power_steering',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='preview_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='saleads',
            name='rain_sensing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='road_no',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='sensing_lock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='shop_no',
            field=models.CharField(default='https://pypi.org/', max_length=120),
        ),
        migrations.AddField(
            model_name='saleads',
            name='state',
            field=models.CharField(default='https://pypi.org/', max_length=120),
        ),
        migrations.AddField(
            model_name='saleads',
            name='trunk_light',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='twitter',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='vanity_mirror',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleads',
            name='video_url',
            field=models.CharField(default='https://pypi.org/', max_length=1024),
        ),
        migrations.AddField(
            model_name='saleads',
            name='ward_no',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='web_site',
            field=models.CharField(default='https://pypi.org/', max_length=120),
        ),
        migrations.AddField(
            model_name='saleads',
            name='whatsapp',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='saleads',
            name='youtube',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='imageingallery',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_in_gallery', to='site_track.saleads'),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_colour',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_condition',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_fuel',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_make',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_millage',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_price_type',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='vehicle_type',
            field=models.CharField(default='https://pypi.org/', max_length=60),
        ),
        migrations.DeleteModel(
            name='VehicleFeatures',
        ),
        migrations.DeleteModel(
            name='VehiclePhotoVideo',
        ),
        migrations.DeleteModel(
            name='VendorAddress',
        ),
    ]
