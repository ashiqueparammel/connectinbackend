from django.apps import AppConfig


class CompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'company'

    def ready(self):
        import company.signals  # This is where you import and connect your signals
