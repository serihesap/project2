# Generated by Django 3.0.3 on 2020-05-01 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contactform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contact',
        ),
    ]