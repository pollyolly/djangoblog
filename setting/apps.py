from django.apps import AppConfig


class SettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'setting'
    verbose_name = ' App Settings'

class AuthConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'django.contrib.auth'
   verbose_name = '  User Settings'
