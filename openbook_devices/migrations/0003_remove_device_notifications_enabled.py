# Generated by Django 2.1.5 on 2019-03-03 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_devices', '0002_device_notifications_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='notifications_enabled',
        ),
    ]