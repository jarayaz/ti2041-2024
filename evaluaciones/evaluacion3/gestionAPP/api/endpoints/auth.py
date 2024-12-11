from ninja import Router
from django.contrib.auth import authenticate
from ..schemas.auth import TokenSchema, TokenResponseSchema
import jwt
from django.conf import settings

router = Router()

@router.post("/token", response=TokenResponseSchema)
def get_token(request, credentials: TokenSchema):
    user = authenticate(username=credentials.username, password=credentials.password)
    if user:
        token = jwt.encode(
            {"user_id": user.id},
            settings.SECRET_KEY,
            algorithm="HS256"
        )
        return {"token": token}
    return {"error": "Invalid credentials"}
