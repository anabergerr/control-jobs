from sqlalchemy.orm import Session

from adapters.persistence.models.model_user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_google_id(self, google_id: str):
        return self.db.query(User).filter(User.google_id == google_id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(
        self,
        name: str,
        email: str,
        google_id: str = None,
        password_hash: str = None,
        created_at=None,
    ) -> User:
        user = User(
            name=name,
            email=email,
            google_id=google_id,
            password_hash=password_hash,
            created_at=created_at,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
