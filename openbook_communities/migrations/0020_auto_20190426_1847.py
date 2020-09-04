# Generated by Django 2.2 on 2019-04-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0019_auto_20190426_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitylog',
            name='action_type',
            field=models.CharField(choices=[('B', 'Ban'), ('U', 'Unban'), ('AM', 'Add Moderator'), ('RM', 'Remove Moderator'), ('AA', 'Add Administrator'), ('RA', 'Remove Administrator'), ('OP', 'Open Post'), ('CP', 'Close Post'), ('RP', 'Remove Post'), ('RPC', 'Remove Post Comment'), ('DPC', 'Disable Post Comments'), ('EPC', 'Enable Post Comments')], editable=False, max_length=5),
        ),
    ]