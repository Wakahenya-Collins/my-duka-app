
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class MyDukaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mydukaapp'

    def ready(self):
        import mydukaapp.signals
