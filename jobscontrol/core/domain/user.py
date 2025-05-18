from dataclasses import dataclass, field
from datetime import datetime

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclass
class User:
    id: int
    name: str
    email: str
    password_hash: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password_hash)

    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)
