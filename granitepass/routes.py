"""
Routine responsible for web routes.
"""
from flask import Blueprint


class RouteHandler:
    def __init__(self):
        self.__main = Blueprint('main', __name__)

    @property
    def main(self):
        return self.__main

    # @main.setter
    # def main(self, page):
    #     self.__main.route(page.endpoint)

    def add_routes(self, page):
        self.main.route(page.route)(page.get_content)
