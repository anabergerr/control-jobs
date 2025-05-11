from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from adapters.persistence.user_repository_impl import UserRepository
from database.database import SessionLocal
from infrastructure.auth.auth_config import oauth
from core.services.jwt_service import create_jwt_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/auth")
async def auth(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)

    user_repo = UserRepository(db)
    user = user_repo.get_by_google_id(user_info["sub"])

    if not user:
        user = user_repo.create_user(
            name=user_info["name"], email=user_info["email"], google_id=user_info["sub"]
        )

    jwt_token = create_jwt_token({"sub": user.google_id, "email": user.email})

    return {
        "access_token": jwt_token,
        "user": {"id": user.id_user, "email": user.email, "name": user.name},
    }
