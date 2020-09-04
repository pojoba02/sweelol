# Generated by Django 2.1.4 on 2019-01-03 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_invitations', '0005_userinvite_invite_email_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvite',
            name='created_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
