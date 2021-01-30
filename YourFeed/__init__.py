from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from YourFeed.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

# login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    from .main.routes import main

    app.register_blueprint(main)

    return app
