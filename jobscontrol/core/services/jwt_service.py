from datetime import datetime, timedelta

from jose import jwt

SECRET_KEY = "SUA_CHAVE_SECRETA"
ALGORITHM = "HS256"


def create_jwt_token(data: dict, expires_in_hours: int = 2):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=expires_in_hours)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
