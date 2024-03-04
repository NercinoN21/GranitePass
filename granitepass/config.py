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
