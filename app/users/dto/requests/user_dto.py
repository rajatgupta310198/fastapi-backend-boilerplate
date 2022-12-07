from pydantic import constr
from pydantic import EmailStr

from app.dto import BaseRequestDto


class UserSignUpDto(BaseRequestDto):
    email: EmailStr
    name: str
    password: constr(strip_whitespace=True, min_length=5)
