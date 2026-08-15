from django.apps import AppConfig
from django.core.signals import request_finished


class AuthenticationsConfig(AppConfig):
    name = 'authentications'
    verbos_name='authentications'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals  # noqa

        # Explicitly connect a signal handler.
        #request_finished.connect(signals.password_reset_token_created(reset_password_token=None))
