from datetime import datetime, timedelta
from ninja.security import HttpBearer
import jwt
from django.conf import settings

def create_token(user):
    exp = datetime.now() + timedelta(days=1)
    return jwt.encode(
        {
            'user_id': user.id,
            'exp': exp,
            'type': 'access'
        },
        settings.SECRET_KEY,
        algorithm='HS256'
    )

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
