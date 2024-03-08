"""
Routine responsible for controlling the DataBase class.
"""
from typing import List

from granitepass.config import Config
from granitepass.database import DataBase
from granitepass.encryption import Encryption

CONFIG = Config()


class LoginDataBase:
    """Class to control login interaction with the DataBase"""

    def __init__(self, user: str, password: str):
        """Initialize the class with the user and password"""
        self.__key_table = CONFIG.key_login_table
        self.__str_password = CONFIG.str_password
        self.__user = user
        self.__password = password
        self.__table = CONFIG.tables[self.key_table]

    @property
    def key_table(self) -> str:
        return self.__key_table

    @property
    def str_password(self) -> str:
        return self.__str_password

    @property
    def user(self) -> str:
        return self.__user

    @property
    def password(self) -> str:
        return self.__password

    @property
    def table(self) -> str:
        return self.__table

    def validate_login(self) -> bool:
        """Controls login validation"""
        db = DataBase()
        user = db.get_data(self.table, user=self.user)
        if user:
            encryption = Encryption(
                user[0][self.str_password], user[0]['salt']
            )
            return encryption.verify_password(
                self.password, user[0][self.str_password]
            )
        return False


class HomePageDataBase:
    """Class to control HomePage interaction with the DataBase"""

    def __init__(self, user: str) -> None:
        """Initialize the class with the user and table"""
        self.__key_table = CONFIG.key_credential_table
        self.__user = user
        self.__table = CONFIG.tables[self.key_table]

    @property
    def key_table(self) -> str:
        return self.__key_table

    @property
    def user(self) -> str:
        return self.__user

    @property
    def table(self) -> str:
        return self.__table

    def credentials(self) -> List[dict]:
        """Get the credentials from the user account"""
        db = DataBase()

        results = db.get_data(self.table, linked_user_account=self.user)

        login = db.get_data(
            CONFIG.tables[CONFIG.key_login_table], user=self.user
        )[0]
        if results:
            encryption = Encryption(
                login[CONFIG.str_password], login[CONFIG.str_salt]
            )
            for result in results:
                result[CONFIG.str_site] = (
                    f'{CONFIG.str_site.capitalize()}: '
                    + result[CONFIG.str_site]
                )
                result[CONFIG.str_user] = (
                    f'{CONFIG.str_user.capitalize()}: '
                    + result[CONFIG.str_user]
                )
                result[CONFIG.str_password] = (
                    f'{CONFIG.str_password.capitalize()}: '
                    + encryption.decrypt_password(result[CONFIG.str_password])
                )

        return results

    def search(self, search) -> List[dict]:
        """Get the credentials according to the search"""
        results = self.credentials()

        return [
            result
            for result in results
            if search
            in result[CONFIG.str_site].replace(f'{CONFIG.str_site}: ', '')
        ]
