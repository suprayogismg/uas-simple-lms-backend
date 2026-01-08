from ninja.security import HttpBearer
from .auth_utils import jwt
from django.conf import settings

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            request.user_role = payload["role"]
            return payload
        except:
            return None
