import re
from fastapi.requests import Request
from app.exceptions.exceptions import UnauthorizedException

from app.settings import AppConfigSettings

class AuthService:


    def __init__(self) -> None:
        pass

    @classmethod
    def extract_token(request: Request):
        token: str = request.headers.get("authorization")
        if not token:
            raise UnauthorizedException()
        return re.sub(AppConfigSettings.JWT_REGEX, "", token, 0, re.MULTILINE)
    