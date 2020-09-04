# Generated by Django 2.2.4 on 2019-08-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0045_auto_20190821_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='openbook_posts.Post'),
        ),
        migrations.AlterField(
            model_name='postmedia',
            name='type',
            field=models.CharField(choices=[('V', 'Video'), ('I', 'Image')], max_length=5),
        ),
    ]
