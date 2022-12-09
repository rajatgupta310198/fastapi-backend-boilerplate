from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from app.auth.auth_service import AuthService
from app.deps import get_db
from app.users.dto.requests.auth_dto import LoginDto
from app.users.dto.responses.auth_dto import TokenResponse

auth_api = APIRouter(prefix="/auth", tags=["Authentication APIs"])


@auth_api.post("/login", status_code=status.HTTP_200_OK, response_model=TokenResponse)
def login(body: LoginDto, db: Session = Depends(get_db)):
    """API to give tokens to user."""
    print(body)
    tokens = AuthService.initiate_login(body=body, db=db)

    return tokens
