from datetime import datetime
from .settings import api_settings
import jwt


def gen_jwt(user):
    payload = {'id': user.id, 'iat': datetime.utcnow()}
    encoded = jwt.encode(payload, api_settings.JWT_SECRET_KEY, algorithm='HS256').decode()
    encoded = encoded.split('.', 1)[1]  # no header
    return {'jwt': encoded}  # the user.id is in the token at field "id"
    # return {'jwt': encoded, 'userId': user.id}
