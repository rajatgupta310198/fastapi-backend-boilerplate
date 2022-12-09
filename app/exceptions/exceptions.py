"""Declare all your exceptions here which can be used across project."""
from fastapi import HTTPException
from fastapi import status


class UnauthorizedException(HTTPException):
    """Unauthorized exception."""

    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail=None,
        headers=None,
    ):
        super().__init__(status_code, detail=detail, headers=headers)


class AlreadyExistsException(HTTPException):
    """AlreadyExists exception."""

    def __init__(
        self,
        status_code: int = status.HTTP_409_CONFLICT,
        detail=None,
        headers=None,
    ):
        super().__init__(status_code, detail=detail, headers=headers)


class DoesNotExistsException(HTTPException):
    """Does not exists exception."""

    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail=None,
        headers=None,
    ):
        super().__init__(status_code, detail=detail, headers=headers)


class InvalidCredentialsException(HTTPException):
    """Invalid credential exception."""

    def __init__(
        self,
        status_code: int = status.HTTP_406_NOT_ACCEPTABLE,
        detail=None,
        headers=None,
    ):
        super().__init__(status_code, detail=detail, headers=headers)
