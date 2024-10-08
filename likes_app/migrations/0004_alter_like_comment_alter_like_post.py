# Generated by Django 5.1 on 2024-09-04 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0002_alter_comment_post_alter_comment_user'),
        ('likes_app', '0003_alter_like_comment_alter_like_post'),
        ('publication_app', '0007_rename_image_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='comments_app.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='publication_app.post'),
        ),
    ]
