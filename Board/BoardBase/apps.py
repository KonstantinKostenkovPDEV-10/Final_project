from django.apps import AppConfig


class BoardbaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BoardBase'

    def ready(self):
        import BoardBase.signals