# app/auth/dependencies.py
from fastapi import Depends, Header, HTTPException, status
from app.core.security import verify_jwt

async def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format",
        )

    token = authorization.split(" ", 1)[1].strip()
    payload = verify_jwt(token)

    user_id = payload.get("sub")
    email = payload.get("email")
    role = payload.get("role", "authenticated")  # Supabase default role

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject (sub)",
        )

    return {
        "user_id": user_id,
        "email": email,
        "role": role,
        "raw": payload,
    }
