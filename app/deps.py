import jwt
from app.auth.auth_service import AuthService
from app.databases.db import SessionLocal
from app.dto.core_dto import CurrentUser
from app.exceptions.exceptions import UnauthorizedException
from app.settings import AppConfigSettings


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



def get_current_user(request) -> CurrentUser:

    """Method to verify token.
    :param request: Request
    :return CurrentUser
    """
    token = AuthService.extract_token(request)
    try:
        decoded = jwt.decode(
            token,
            AppConfigSettings.ACCESS_SECRET,
            algorithms=AppConfigSettings.JWT_ALGO,
        )
        decoded.pop("issuer")
        decoded.pop("exp")

    except jwt.exceptions.ExpiredSignatureError:
        raise UnauthorizedException(detail="expired")
    # user = UserService.get_user_by_id(decoded.get("user_id"))
    # if not user:
    #     raise UnauthorizedException(detail="user with this token does not exists")
    return CurrentUser(id=decoded.get("id"))