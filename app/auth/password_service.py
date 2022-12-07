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

    def __init__(self, in_pass: str, second_pass: str = None) -> None:
        self.in_pass = in_pass
        self.second_pass = second_pass
        self.salt = AppConfigSettings.PASSWORD_SALT

    def verify_password(self) -> bool:
        return (
            PasswordService.generate_key(self.in_pass).decode()
            == PasswordService.encrypt_password(self.second_pass).decode()
        )

    def encrypt_password(self) -> bytes:
        return PasswordService.generate_key(self.in_pass)
