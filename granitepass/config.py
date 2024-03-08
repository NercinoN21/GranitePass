"""
Routine responsible for general configuration.
"""
import os


class Config:
    """Responsible for project's configuration"""

    def __init__(self):
        """Configuration variables"""
        self.__project_name = 'GranitePass'
        self.__index_route = '/'
        self.__index_controller = 'index_controller'
        self.__str_password = 'password'
        self.__str_site = 'site'
        self.__str_user = 'user'
        self.__str_login = 'login'
        self.__str_salt = 'salt'
        self.__str_search = 'search'
        self.__str_current_user = 'current_user'
        self.__enter_btn = 'go!'
        self.__login_page = 'login.html'
        self.__login_route = '/login/'
        self.__login_controller = 'login_controller'
        self.__data_dir = 'database'
        self.__data_file = 'db.json'
        self.__key_login_table = 'login'
        self.__key_credential_table = 'credential'
        self.__tables = self.__generate_tables(
            table01=self.key_login_table, table02=self.key_credential_table
        )
        self.__code = 'utf-8'
        self.__home_page_controller = 'home_page_controller'
        self.__method_post = 'POST'
        self.__homepage_page = 'homepage.html'

    def __repr__(self) -> str:
        """Basic instance representation"""
        return f'{self.__dict__}'

    def __str__(self) -> str:
        """Print representation"""
        return f'{self.__dict__}'

    @property
    def project_name(self) -> str:
        return self.__project_name

    @property
    def index_route(self) -> str:
        return self.__index_route

    @property
    def index_controller(self) -> str:
        return self.__index_controller

    @property
    def str_site(self) -> str:
        return self.__str_site

    @property
    def str_password(self) -> str:
        return self.__str_password

    @property
    def str_user(self) -> str:
        return self.__str_user

    @property
    def str_login(self) -> str:
        return self.__str_login

    @property
    def str_salt(self) -> str:
        return self.__str_salt

    @property
    def str_search(self) -> str:
        return self.__str_search

    @property
    def str_current_user(self) -> str:
        return self.__str_current_user

    @property
    def enter_btn(self) -> str:
        return self.__enter_btn

    @property
    def login_page(self) -> str:
        return self.__login_page

    @property
    def login_route(self) -> str:
        return self.__login_route

    @property
    def login_controller(self) -> str:
        return self.__login_controller

    @property
    def data_dir(self) -> str:
        return self.__data_dir

    @property
    def data_file(self) -> str:
        return self.__data_file

    @property
    def key_login_table(self) -> str:
        return self.__key_login_table

    @property
    def key_credential_table(self) -> str:
        return self.__key_credential_table

    @property
    def tables(self) -> dict[str, str]:
        return self.__tables

    @property
    def db_file(self) -> str:
        return os.path.join(self.data_dir, self.data_file)

    @property
    def code(self) -> str:
        return self.__code

    @property
    def home_page_controller(self) -> str:
        return self.__home_page_controller

    @property
    def method_post(self) -> str:
        return self.__method_post

    @property
    def homepage_page(self) -> str:
        return self.__homepage_page

    def __generate_tables(self, **kwargs) -> dict[str, str]:
        return {key: f'{key}_table' for key in kwargs.values()}
