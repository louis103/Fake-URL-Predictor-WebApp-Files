from flask import Blueprint,render_template,request,flash,jsonify,make_response,redirect,send_file,url_for,Response
from flask_login import login_manager,login_required,current_user
from .models import User,Urls
from .models import db
import pickle
import os
import requests
from urllib.parse import urlparse


views = Blueprint('views',__name__)

#init our model
basedir = os.path.abspath(os.path.dirname(__file__))
model_path = "static/ml_models/phishing-sites.pkl"
folder = os.path.join(basedir,model_path)
#using pickle to load our model
model = pickle.load(open(folder, 'rb'))

@views.route('/')
@views.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        url_string = request.form.get("url_input")
        if "http://" in url_string:
            new_url = url_string.replace("http://","",1)
        else:
            new_url = url_string.replace("https://","",1)
        #preparing our url
        url = [new_url]
        results = model.predict(url)
        #checking for url redirects
        url_array = []
        try:
            responses = requests.get(url_string,allow_redirects=True,timeout=2.5)
            for response in responses.history:
                url_array.append(response.url)
                if(len(url_array)<=0):
                    url_array.append("None")
        except requests.exceptions.ConnectionError:
            url_array.append("Oops! No redirects found!")
        
        urldir = urlparse(url_string).path
        count = urldir.count('/')
        letters = 0
        for i in url_string:
            if i.isalpha():
                letters = letters + 1
        length = len(str(url_string))
        return render_template("home.html",results=results[0],redirects=url_array,main_url=url_string,length=length)
        #disposing predicted results to the user
    
    return render_template("home.html")