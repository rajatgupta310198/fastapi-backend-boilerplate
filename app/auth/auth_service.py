import re
from datetime import datetime
from datetime import timedelta

import jwt
from fastapi.requests import Request
from sqlalchemy.orm import Session

from app.exceptions.exceptions import DoesNotExistsException
from app.exceptions.exceptions import InvalidCredentialsException
from app.exceptions.exceptions import UnauthorizedException
from app.settings import AppConfigSettings
from app.users.dto.requests.auth_dto import LoginDto
from app.users.models import User


class AuthService:
    def __init__(self) -> None:
        pass

    @classmethod
    def extract_token(request: Request):
        token: str = request.headers.get("authorization")
        if not token:
            raise UnauthorizedException()
        return re.sub(AppConfigSettings.JWT_REGEX, "", token, 0, re.MULTILINE)

    @staticmethod
    def prepara_tokens(user: User):
        payload = {
            "id": str(user.id),
            "issuer": "backend",
            "exp": datetime.utcnow() + timedelta(days=1),
        }

        access_token = jwt.encode(
            payload,
            AppConfigSettings.ACCESS_SECRET,
            algorithm=AppConfigSettings.JWT_ALGO,
        )

        payload.__setitem__("exp", datetime.utcnow() + timedelta(days=30))

        refresh_token = jwt.encode(
            payload,
            AppConfigSettings.REFRESH_SECRET,
            algorithm=AppConfigSettings.JWT_ALGO,
        )
        return access_token, refresh_token

    @staticmethod
    def initiate_login(body: LoginDto, db: Session):
        user = db.query(User).filter_by(email=body.email).first()
        if not user:
            raise DoesNotExistsException(
                detail=f"User with email {body.email} does not exists",
            )
        from .password_service import PasswordService

        password_service = PasswordService()
        if not password_service.verify_password(
            password_entered=body.password,
            actual_password=user.password,
        ):
            raise InvalidCredentialsException(detail="Invalid credential")
        # prepare tokens
        access_token, refresh_token = AuthService.prepara_tokens(user=user)
        return dict(access_token=access_token, refresh_token=refresh_token)
