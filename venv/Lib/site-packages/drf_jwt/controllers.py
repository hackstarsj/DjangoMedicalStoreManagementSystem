from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from rest_framework import status, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response


from .validators import Credentials
from .authentication import JSONWebTokenAuthentication
from .utils import gen_jwt


class Auth(APIView):
    # overide to escape permission and authentication
    permission_classes = [permissions.AllowAny]  # ⸄()⸅ works too
    authentication_classes = [authentication.BasicAuthentication, JSONWebTokenAuthentication]

    def get(self, request, format=None):
        # check for authentication:
        if isinstance(request.user, AnonymousUser):
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED,
                            headers={'WWW-Authenticate': 'Basic realm="api"'})
        return Response(self.gen_jwt(request.user))

    def post(self, request, format=None):
        login_credentials = Credentials(data=request.data)
        login_credentials.is_valid(raise_exception=True)

        return response_jwt_from_credentials(login_credentials)


def response_jwt_from_credentials(credentials):
    user = authenticate(**credentials.data)
    if user is None:
        msg = 'Unable to log in with provided credentials.'
        return Response({'detail': msg}, status=status.HTTP_400_BAD_REQUEST)

    if not user.is_active:
        msg = 'User account is disabled.'
        return Response({'detail': msg}, status=status.HTTP_400_BAD_REQUEST)

    return Response(gen_jwt(user))
