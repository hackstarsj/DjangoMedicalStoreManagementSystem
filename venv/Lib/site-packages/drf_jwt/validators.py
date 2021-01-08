from rest_framework import serializers

from .settings import api_settings


class Credentials(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add a field named from api_settings.USER_LOGIN that identify the user
        self.fields[api_settings.USER_LOGIN] = serializers.CharField()

    password = serializers.CharField(style={'input_type': 'password'})
