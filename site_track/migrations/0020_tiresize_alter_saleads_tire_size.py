# Generated by Django 4.0.4 on 2023-01-20 09:19

from django.db import migrations, models
import django.db.models.deletion
import site_track.models


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0019_typeof5wheel_alter_saleads_type_of_5_wheel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TireSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            bases=(models.Model, site_track.models.ChoicesMixin),
        ),
        migrations.AlterField(
            model_name='saleads',
            name='tire_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_ads', to='site_track.tiresize'),
        ),
    ]
