# app/auth/rbac.py
from fastapi import HTTPException, status

def require_role(*allowed_roles):
    def checker(user: dict):
        if user.get("role") not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden",
            )
        return user
    return checker
