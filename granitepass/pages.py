"""
Routine responsible for modeling pages.
"""
from flask import render_template
from granitepass.config import Config

class loginPage:
    def __init__(self, config: Config):
        self.__login_page = config.login_page
        self.__enter_btn = config.enter_btn
        self.__title = config.project_name
        self.__password = config.password
        self.__user = config.user

    def get_content(self):
        return render_template(self.__login_page, 
                               user = self.__user, 
                               password = self.__password,
                               enter_btn = self.__enter_btn,
                               title = self.__title)