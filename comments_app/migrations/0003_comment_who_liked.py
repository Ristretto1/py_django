# Generated by Django 5.1 on 2024-09-06 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0002_alter_comment_post_alter_comment_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='who_liked',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
