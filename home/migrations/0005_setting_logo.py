# Generated by Django 3.0.3 on 2020-04-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_setting_welcome_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
