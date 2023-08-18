from app.dto import BaseResponseDto


class TokenResponse(BaseResponseDto):
    access_token: str
    refresh_token: str
