from fastapi import APIRouter, Request

from infrastructure.auth.auth_config import oauth

router = APIRouter()


@router.get("/login")
async def login(request: Request):
    redirect_uri = "http://localhost:8000/auth"  # ou use uma ENV
    return await oauth.google.authorize_redirect(request, redirect_uri)
