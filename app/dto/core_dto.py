from uuid import UUID

from pydantic import BaseModel
from pydantic import Extra


class BaseResponseDto(BaseModel):
    class Config:
        from_attributes = True


class BaseRequestDto(BaseModel):
    class Config:
        str_strip_whitespace = True
        extra = Extra.forbid


class CurrentUser(BaseModel):
    id: UUID
