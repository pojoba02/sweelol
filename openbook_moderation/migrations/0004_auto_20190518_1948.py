# Generated by Django 2.2 on 2019-05-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_moderation', '0003_moderatedobject_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderatedobjectdescriptionchangedlog',
            name='changed_from',
            field=models.CharField(max_length=1000, null=True, verbose_name='changed from'),
        ),
        migrations.AlterField(
            model_name='moderatedobjectdescriptionchangedlog',
            name='changed_to',
            field=models.CharField(max_length=1000, null=True, verbose_name='changed to'),
        ),
    ]
