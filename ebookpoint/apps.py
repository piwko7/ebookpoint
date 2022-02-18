from django.apps import AppConfig


class EbookpointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ebookpoint'

    def ready(self):
    	from jobs import updater
    	updater.start()
