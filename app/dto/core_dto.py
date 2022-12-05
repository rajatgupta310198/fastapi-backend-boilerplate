from uuid import UUID

from pydantic import BaseModel


class BaseResponseDto(BaseModel):
    class Config:
        orm_mode = True


class CurrentUser(BaseModel):
    id: UUID
