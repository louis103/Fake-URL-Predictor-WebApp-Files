from flask import Flask,Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_manager,login_required,logout_user,current_user
from .models import User,Urls
from . import db
auth = Blueprint('auth',__name__)