import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from app.settings import AppConfigSettings


class PasswordService:
    @staticmethod
    def generate_key(in_string: str, salt: str = None) -> bytes:
        if not salt:
            salt = AppConfigSettings.PASSWORD_SALT
        kdf = PBKDF2HMAC(
            algorithm=SHA256,
            length=32,
            salt=salt.encode(),
            iterations=38000,
            backend=default_backend(),
        )
        key = base64.urlsafe_b64encode(kdf.derive(in_string.encode()))
        return key

    def __init__(self) -> None:
        self.salt = AppConfigSettings.PASSWORD_SALT

    def verify_password(self, password_entered: str, actual_password: str) -> bool:
        return (
            PasswordService.generate_key(password_entered).decode() == actual_password
        )

    def encrypt_password(self, password: str) -> bytes:

        return PasswordService.generate_key(password)
