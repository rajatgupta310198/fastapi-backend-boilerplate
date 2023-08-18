from pydantic import constr
from pydantic import EmailStr

from app.dto import BaseRequestDto


class LoginDto(BaseRequestDto):
    email: EmailStr
    password: constr(min_length=6)
