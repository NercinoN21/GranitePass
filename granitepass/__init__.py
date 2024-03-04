"""
Routine responsible for adding configurations and registering blueprints.
"""
from flask import Flask
from granitepass.config import Config
from granitepass.routes import RouteHandler
from granitepass.pages import loginPage


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    route_handler = RouteHandler()
    route_handler.add_routes(loginPage(Config()))
    app.register_blueprint(route_handler.main)
    return app
