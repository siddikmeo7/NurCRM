from django.apps import AppConfig


class NurcrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NurCRM'
    
    def ready(self):
        import NurCRM.signals
