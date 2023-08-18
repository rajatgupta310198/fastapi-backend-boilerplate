from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from app.auth.auth_service import AuthService
from app.deps import get_db
from app.v1.users.dto.requests import LoginDto
from app.v1.users.dto.responses import TokenResponse

auth_api = APIRouter(tags=["Authentication APIs"])


@auth_api.post("/login", status_code=status.HTTP_200_OK, response_model=TokenResponse)
def login(body: LoginDto, db: Session = Depends(get_db)):
    """API to give tokens to user."""
    tokens = AuthService.initiate_login(body=body, db=db)

    return {}
