from fastapi import APIRouter

from .users.routes import auth_api as auth_api_v1
from .users.routes import user_api as user_api_v1

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(user_api_v1, prefix="/users")
v1_router.include_router(auth_api_v1, prefix="/auth")
