import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MIN"))

def create_access_token(subject: str, role: str):
    to_encode = {
        "sub": subject,     # users email 
        "role": role,       # student or teacher
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "iat": datetime.utcnow()
    }
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        print('Access Token decoding error')
        return None