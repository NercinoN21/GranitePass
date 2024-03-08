"""
Routine responsible for controlling web routes.
"""
from flask import redirect, render_template, request, url_for
from flask.views import View

from granitepass.config import Config
from granitepass.database_controllers import HomePageDataBase, LoginDataBase

CONFIG = Config()


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
        if request.method == CONFIG.method_post:
            form_user = request.form[CONFIG.str_user]
            form_password = request.form[CONFIG.str_password]

            login_database = LoginDataBase(form_user, form_password)

            if login_database.validate_login():
                return redirect(
                    url_for(
                        CONFIG.home_page_controller,
                        **{CONFIG.str_user: form_user}
                    )
                )

            return redirect(url_for(CONFIG.login_controller))
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
        user = request.args.get(CONFIG.str_user)

        credentials = HomePageDataBase(user).credentials()

        return render_template(
            CONFIG.homepage_page,
            credentials=credentials,
            title=CONFIG.project_name,
            current_user=user,
        )


class HomePageSearchController(View):
    def dispatch_request(self):
        if request.method == CONFIG.method_post:
            form_search = request.form[CONFIG.str_search]
            form_current_user = request.form.get(CONFIG.str_current_user)

            filter_credentials = HomePageDataBase(form_current_user).search(
                form_search
            )

        return render_template(
            CONFIG.homepage_page,
            credentials=filter_credentials,
            site=form_search,
            title=CONFIG.project_name,
            current_user=form_current_user,
        )
