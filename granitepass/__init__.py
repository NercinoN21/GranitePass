from flask import Flask
from .route_controllers import IndexController, LoginController
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

    return app
