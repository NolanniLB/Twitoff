from flask import Flask
from .db_model import db

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/nolanni/Twitoff/twitoff/web_app_99.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'
    return app