# Generated by Django 2.1.4 on 2019-01-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_common', '0009_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='keyword',
            field=models.CharField(max_length=16, unique=True, verbose_name='keyword'),
        ),
    ]
