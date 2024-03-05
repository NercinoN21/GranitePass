from flask import Flask
from .route_controllers import HomePageSearchController,IndexController, LoginController, HomePageController
from granitepass.config import Config


CONFIG = Config()


def create_app():
    app = Flask(__name__)
    app.add_url_rule(
        CONFIG.index_route,
        view_func=IndexController.as_view(CONFIG.index_controller),
    )
    app.add_url_rule(
        CONFIG.login_route,
        view_func=LoginController.as_view(CONFIG.login_controller),
        methods=['GET', 'POST'],
    )
    app.add_url_rule(
        '/HomePage',
        view_func=HomePageController.as_view("home_page_controller"),
        methods=['GET', 'POST'],
    )
    app.add_url_rule(
        '/HomePageSearch',
        view_func=HomePageSearchController.as_view("home_page_search_controller"),
        methods=['POST'],
    )


    return app
