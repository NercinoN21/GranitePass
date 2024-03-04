"""
Routine responsible for general configuration.
"""
import os


class Config:
    def __init__(self):
        self.__project_name = 'GranitePass'
        self.__index_route = '/'
        self.__index_controller = 'index_controller'
        self.__str_password = 'password'
        self.__str_user = 'user'
        self.__enter_btn = 'go!'
        self.__login_page = 'login.html'
        self.__login_route = '/login/'
        self.__login_controller = 'login_controller'
        self.__data_dir = 'database'
        self.__data_file = 'db.json'
        self.__tables = ['login', 'credential']

    def __str__(self):
        return f'{self.__dict__}'

    @property
    def project_name(self):
        return self.__project_name

    @property
    def index_route(self):
        return self.__index_route

    @property
    def index_controller(self):
        return self.__index_controller

    @property
    def str_password(self):
        return self.__str_password

    @property
    def str_user(self):
        return self.__str_user

    @property
    def enter_btn(self):
        return self.__enter_btn

    @property
    def login_page(self):
        return self.__login_page

    @property
    def login_route(self):
        return self.__login_route

    @property
    def login_controller(self):
        return self.__login_controller

    @property
    def data_dir(self):
        return self.__data_dir

    @property
    def data_file(self):
        return self.__data_file

    @property
    def tables(self):
        return self.__tables

    @property
    def db_file(self):
        return os.path.join(self.data_dir, self.data_file)
