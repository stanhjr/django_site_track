# Generated by Django 4.0.4 on 2022-06-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0047_rename_settingsheaderinventoryaboutus_settingsheaderaboutus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsAuthBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Lorem ipsum dolor sit amet consectetur adipisicing')),
                ('text', models.TextField(default='Elit Iusto dolore libero recusandae dolor dolores explicabo ullam cum facilis aperiam alias odio quam excepturi molestiae omnis inventore. Repudiandae officiaplaceat amet consectetur dicta dolorem quo')),
            ],
        ),
    ]
