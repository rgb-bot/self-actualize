from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .config import SQLALCHEMY_DATABASE_URI


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    # Initialize the SQLAlchemy instance with the app
    db.init_app(app)

    return app
