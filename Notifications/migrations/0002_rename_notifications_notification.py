# Generated by Django 3.2.12 on 2023-08-04 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
    ]
