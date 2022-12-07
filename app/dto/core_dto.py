from uuid import UUID

from pydantic import BaseModel
from pydantic import Extra


class BaseResponseDto(BaseModel):
    class Config:
        orm_mode = True


class BaseRequestDto(BaseModel):
    class Config:
        anystr_strip_whitespace = True
        extra = Extra.forbid


class CurrentUser(BaseModel):
    id: UUID
