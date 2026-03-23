from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth.schemas import UserCreate, UserRead, TokenWithRefresh, Token
from app.auth.deps import authenticate_user, get_current_user, require_roles
from app.auth.services import AuthService
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

##register endpoint -assigned to Deepa##
#@router.post("/register", response_model=UserRead)
#def register(
    #user_in: UserCreate,
    #db: Session = Depends(get_db),
#):
    #service = AuthService(db)
    #3#existing = db.query(User).filter(User.email == user_in.email).first()
    #if existing:
        #raise HTTPException(status_code=400, detail="Email already registered")
    #user = service.register_user(user_in)
    #return user


@router.post("/login", response_model=TokenWithRefresh)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    service = AuthService(db)
    access_token, refresh_token = service.create_tokens_for_user(user)
    return TokenWithRefresh(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh", response_model=Token)
def refresh_token(
    refresh_token: str,
    current_user: User = Depends(get_current_user),
):
    # For now, just issue a new access token; in production, validate refresh token from DB
    from app.core.security import create_access_token

    roles = [r.name for r in current_user.roles]
    access_token = create_access_token(subject=current_user.email, roles=roles)
    return Token(access_token=access_token)


@router.post("/logout")
def logout(
    refresh_token: str,
    current_user: User = Depends(get_current_user),
):
    # Stub: if you persist refresh tokens, mark this one revoked
    return {"message": "Logged out"}


@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/admin-only")
def admin_only(current_user: User = Depends(require_roles(["admin"]))):
    return {"message": f"Hello admin {current_user.email}"}
