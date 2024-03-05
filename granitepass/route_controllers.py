"""
Routine responsible for controlling web routes.
"""
from flask import render_template, request, redirect, url_for, jsonify
from flask.views import View
from granitepass.config import Config


CONFIG = Config()
# For Testing
credentials = [
    {'site': 'site1.com', 'user': 'user1', 'password': 'password1'},
    {'site': 'site2.com', 'user': 'user2', 'password': 'password2'},
    {'site': 'site3.com', 'user': 'user3', 'password': 'password3'},
    {'site': 'site4.com', 'user': 'user4', 'password': 'password4'},
    {'site': 'site5.com', 'user': 'user5', 'password': 'password5'},
    {'site': 'site6.com', 'user': 'user6', 'password': 'password6'},
    {'site': 'site6.com', 'user': 'user6', 'password': 'password6'},
    {'site': 'site7.com', 'user': 'user8', 'password': 'password9'}
]


class IndexController(View):
    def dispatch_request(self):
        return redirect(url_for(CONFIG.login_controller))


class LoginController(View):
    def __init__(self):
        self.__title = CONFIG.project_name
        self.__str_user = CONFIG.str_user
        self.__str_password = CONFIG.str_password
        self.__enter_btn = CONFIG.enter_btn
        self.__login_page = CONFIG.login_page
        self.__login_route = CONFIG.login_route

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, func):
        self.__title = func(self.__title)

    @property
    def str_user(self):
        return self.__str_user

    @str_user.setter
    def str_user(self, func):
        self.__str_user = func(self.__str_user)

    @property
    def str_password(self):
        return self.__str_password

    @str_password.setter
    def str_password(self, func):
        self.__str_password = func(self.__str_password)

    @property
    def enter_btn(self):
        return self.__enter_btn

    @enter_btn.setter
    def enter_btn(self, func):
        self.__enter_btn = func(self.__enter_btn)

    @property
    def login_page(self):
        return self.__login_page

    @property
    def login_route(self):
        return self.__login_route

    def __upper(self, value):
        return value.upper()

    def __capitalize(self, value):
        return value.capitalize()

    def dispatch_request(self):
        if request.method == 'POST':
            form_user = request.form[CONFIG.str_user]
            form_password = request.form[CONFIG.str_password]
            print(f'Credentials: {form_user=} and {form_password=}')

            return redirect(url_for('home_page_controller'))
        else:
            self.str_user = self.__capitalize
            self.str_password = self.__capitalize
            self.enter_btn = self.__upper

            return render_template(
                self.__login_page,
                title=self.title,
                user=self.str_user,
                password=self.str_password,
                enter_btn=self.enter_btn,
            )
        

class HomePageController(View):
    def dispatch_request(self):
        return render_template('homepage.html',
                               credentials=credentials)


class HomePageSearchController(View):
    def dispatch_request(self):
        if request.method == 'POST':
            form_search = request.form['search']
            test_filter = [x for x in credentials if form_search in x['site']]

        return render_template('homepage.html',
                               credentials=test_filter,
                               site=form_search,)
