# Generated by Django 4.0.4 on 2022-06-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_track', '0024_rename_footer_about_company_text_settingsfooter_about_company_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settingsfooter',
            old_name='viber_phone',
            new_name='whatsapp_phone',
        ),
    ]
