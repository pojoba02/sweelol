# Generated by Django 2.2 on 2019-05-03 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0031_postcomment_parent_comment'),
        ('openbook_notifications', '0008_auto_20190503_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCommentReplyNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openbook_posts.PostComment')),
            ],
        ),
    ]
