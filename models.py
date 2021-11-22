from . import db
from flask_login import UserMixin
import datetime
import time
from flask_sqlalchemy import SQLAlchemy

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=False)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    admin_status = db.Column(db.Integer,default=0)
    user_urls = db.relationship('Urls')
    def __repr__(self):
        return self.name
    
class Urls(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    url = db.Column(db.String(500),unique=False)
    prediction = db.Column(db.String(20))
    date_reviewed = db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    def __repr__(self):
        return "Url: "+str(id)
    
