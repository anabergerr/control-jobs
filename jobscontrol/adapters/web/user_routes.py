from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request
from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from adapters.persistence.user_repository_impl import UserRepository
from core.services.jwt_service import create_jwt_token
from database.database import SessionLocal
from infrastructure.auth.auth_config import oauth

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Login com Google (callback)
@router.get("/auth")
async def auth(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.userinfo(token=token)

    user_repo = UserRepository(db)
    user = user_repo.get_by_google_id(user_info["sub"])

    if not user:
        user = user_repo.create_user(
            name=user_info["name"], email=user_info["email"], google_id=user_info["sub"]
        )

    jwt_token = create_jwt_token({"sub": user.google_id, "email": user.email})
    return {
        "access_token": jwt_token,
        "user": {"id": user.id, "email": user.email, "name": user.name},
    }


# ✅ Registro de novo usuário tradicional
@router.post("/register")
async def register_user(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not all([name, email, password]):
        print(name, email, password)
        raise HTTPException(
            status_code=400, detail="Nome, email e senha são obrigatórios."
        )

    user_repo = UserRepository(db)
    existing_user = user_repo.get_by_email(email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email já registrado.")

    hashed_password = bcrypt.hash(password)
    user = user_repo.create_user(
        name=name,
        email=email,
        password_hash=hashed_password,
        created_at=datetime.utcnow(),
    )

    token = create_jwt_token({"sub": str(user.id), "email": user.email})
    return {"access_token": token, "user": {"id": user.id, "email": user.email}}


@router.post("/login")
async def login_user(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        raise HTTPException(status_code=400, detail="Email e senha são obrigatórios.")

    user_repo = UserRepository(db)
    user = user_repo.get_by_email(email)

    if not user or not bcrypt.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")

    token = create_jwt_token({"sub": user.id, "email": user.email})
    return {"access_token": token, "user": {"id": user.id, "email": user.email}}
