from django.apps import AppConfig


class LikesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'likes_app'

    def ready(self):
        from . import signals