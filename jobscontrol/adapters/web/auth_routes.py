from fastapi import APIRouter, Request

from infrastructure.auth.auth_config import oauth

router = APIRouter()


@router.get("/login/google")
async def login(request: Request):
    redirect_uri = "http://localhost:8000/auth"
    return await oauth.google.authorize_redirect(request, redirect_uri)
