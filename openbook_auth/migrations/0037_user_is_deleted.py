# Generated by Django 2.2 on 2019-05-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0036_auto_20190502_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='is deleted'),
        ),
    ]
