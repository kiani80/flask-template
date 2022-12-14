__all__ = ['create_app']

from flask import Flask
from extentions import db


def create_app() -> Flask:
    
    app = Flask(__name__)
    # Need this for flask manager cli
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///proxy.db'
    db.init_app(app)
    return app