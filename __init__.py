from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = "Urls.db"

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = ""
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():

        from .views import views
        from .auth import auth
        app.register_blueprint(views,url_prefix="/")
        app.register_blueprint(auth,url_prefix="/")
        
        from .models import User,Urls
        
        create_db(app=app)
        
        return app
    
def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("DB Created !")
