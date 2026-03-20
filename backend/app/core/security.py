# app/core/security.py
from jose import jwt, JWTError
from fastapi import HTTPException, status
from .config import settings

ALGORITHM = "HS256"
# Supabase uses "authenticated" as audience by default, but we’ll disable aud check for now.
AUDIENCE = "authenticated"

def verify_jwt(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.supabase_jwt_secret,
            algorithms=[ALGORITHM],
            options={"verify_aud": False},  # set True + AUDIENCE if you want strict aud check
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
