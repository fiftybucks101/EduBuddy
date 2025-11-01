from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from database.db import get_db
from users.crud import get_user_by_email, create_user
from auth.hashing import hash_password, verify_password
from auth.jwt_handler import create_access_token, decode_token

router = APIRouter(prefix="/auth", tags=["authentication"])


# -------------- Request/Reshpnse Schemas -----------------
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    role: str = "student"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# ------------------ Endpoints ---------------

@router.post("/register", status_code=201)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    user = create_user(db, payload.email, hash_password(payload.password), payload.role)
    return {"id": user.id, "email": user.email, "role": user.role}

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(subject=user.email, role=user.role)
    return TokenResponse(access_token=token)

