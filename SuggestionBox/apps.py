from django.apps import AppConfig

class SuggestionboxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SuggestionBox'

    def ready(self):
        # This tells Django to load your privacy signals once apps are ready
        import signals