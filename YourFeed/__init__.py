from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    from .main.routes import main

    app.register_blueprint(main)

    return app
