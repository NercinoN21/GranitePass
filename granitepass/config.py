"""
Routine responsible for general configuration.
"""
import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.__project_name = os.getenv('PROJECT_NAME')
        self.__data_dir = os.getenv('DATA_DIR')
        self.__data_file = os.getenv('DATA_FILE')
        self.__tables = os.getenv('TABLES')
        self.__password = os.getenv('PASSWORD')
        self.__user = os.getenv('USER')
        self.__enter_btn = os.getenv('ENTER_BTN')
        self.__login_page = os.getenv('LOGIN_PAGE')

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def project_name(self):
        return self.__project_name
    
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

    @property
    def password(self):
        return self.__password
    
    @property
    def user(self):
        return self.__user
    
    @property
    def enter_btn(self):
        return self.__enter_btn
    
    @property
    def login_page(self):
        return self.__login_page