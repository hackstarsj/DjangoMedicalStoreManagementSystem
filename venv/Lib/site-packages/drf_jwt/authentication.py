from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)
from .settings import api_settings
import jwt
from base64 import b64encode
from datetime import timedelta, datetime


class JSONWebTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token content if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """

        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        # jwt_value = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.' + jwt_value
        jwt_value = b64encode('{"typ":"JWT","alg":"HS256"}'.encode()) + b'.' + jwt_value
        payload = self.valide_jwt(jwt_value)
        user = self.get_user(payload)
        return (user, payload)

    def valide_jwt(self, jwt_value):
        """verify the jwt token and return it's decoded value"""
        try:
            payload = jwt.decode(jwt_value, api_settings.JWT_SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignature:
            msg = _('Token has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            msg = _('Token invalid.')
            raise exceptions.AuthenticationFailed(msg)

        expiration = None
        # expiration = timedelta(seconds=40)
        if expiration is not None:
            if datetime.fromtimestamp(payload['iat']) + expiration < datetime.utcnow():
                # expiration on “iat” (Issued At) Claim
                msg = _('Token has expired.')
                raise exceptions.AuthenticationFailed(msg)
        return payload

    def get_user(self, payload):
        """Returns an active user that matches the payload's user id."""
        User = get_user_model()
        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return user

    def get_jwt_value(self, request):
        """
            Clients should authenticate by passing the token key in the "Authorization"
            HTTP header, prepended with `Bearer` and the base64 encoded jwt token:
                Authorization: Bearer <token>
        """
        auth = get_authorization_header(request).split()
        if not auth:
            return None
        if auth[0] != b'Bearer':
            return None
        if len(auth) == 1:
            msg = _('Invalid Authorization header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid Authorization header. Credentials string '
                    'should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)
        return auth[1]

    def authenticate_header(self, request):
        """
            Return a string to be used as the value of the `WWW-Authenticate`
            header in a `401 Unauthenticated` response,
            WWW-Authenticate header that instructs the client how to authenticate,
            or `None` if the authentication scheme should return `403 Permission Denied` responses.
        """
        return 'Bearer realm="api"'
