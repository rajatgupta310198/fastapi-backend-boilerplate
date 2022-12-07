from typing import Optional
from uuid import UUID

from app.dto import BaseResponseDto


class UserResponseDto(BaseResponseDto):
    id: UUID
    name: Optional[str]
