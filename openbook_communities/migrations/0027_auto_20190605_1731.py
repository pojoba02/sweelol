# Generated by Django 2.2 on 2019-06-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0026_community_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='rules',
            field=models.CharField(max_length=5000, null=True, verbose_name='rules'),
        ),
    ]
