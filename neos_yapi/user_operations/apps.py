from django.apps import AppConfig


class UserOperationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_operations'

    def ready(self):
        import user_operations.signals
