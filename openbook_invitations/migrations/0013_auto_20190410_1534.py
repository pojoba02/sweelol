# Generated by Django 2.2 on 2019-04-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_invitations', '0012_auto_20190410_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvite',
            name='name',
            field=models.CharField(blank=True, max_length=192, null=True),
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='nickname',
            field=models.CharField(blank=True, max_length=192, null=True),
        ),
    ]