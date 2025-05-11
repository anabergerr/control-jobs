import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import jwt

load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"


def create_jwt_token(data: dict, expires_in_hours: int = 2):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=expires_in_hours)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
