"""
Routine responsible for security.
"""
import base64

import bcrypt
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from granitepass.config import Config

CONFIG = Config()


class Encryption:
    """Class to interact with the DataBase class in a safe way"""

    def __init__(self, password, salt) -> None:
        """Generating cipher suite with the password and salt"""
        self.__password = password
        self.__salt = salt
        self.__cipher_suite = self.__derive_key()
        self.__code = CONFIG.code

    def __repr__(self) -> str:
        """Basic instance representation"""
        return f'{self.__dict__}'

    def __str__(self) -> str:
        """Print representation"""
        return f'{self.__dict__}'

    @property
    def password(self) -> str:
        return self.__password.encode()

    @property
    def salt(self) -> str:
        return self.__salt.encode()

    @property
    def cipher_suite(self) -> Fernet:
        return self.__cipher_suite

    @property
    def code(self) -> str:
        return self.__code

    def __derive_key(self, iterations: int = 100_000) -> Fernet:
        """Create cipher suite from a regular password"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=iterations,
            backend=default_backend(),
        )

        key = kdf.derive(self.password)
        key64 = base64.urlsafe_b64encode(key)
        cipher_suite = Fernet(key64)

        return cipher_suite

    def encrypt_password(self, password: str) -> str:
        """Encrypt a password with the cipher suite"""
        return self.cipher_suite.encrypt(password.encode(self.code)).decode(
            self.code
        )

    def decrypt_password(self, password: str) -> str:
        """Decrypt a password with the cipher suite"""
        return self.cipher_suite.decrypt(password.encode(self.code)).decode(
            self.code
        )

    def verify_password(self, password, hashed_password) -> bool:
        """Check if the password is valid"""
        return bcrypt.checkpw(
            password.encode(self.code), hashed_password.encode(self.code)
        )
