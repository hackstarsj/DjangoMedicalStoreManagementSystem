from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

DEFAULTS = {
    'USER_LOGIN': 'username',
    'JWT_SECRET_KEY': settings.SECRET_KEY,
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
)
api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
