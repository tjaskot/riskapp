#########################
### Imported packages ###
# Flask
# flask_login - loginManager, UserMixin (provides boilerplate 4 base methods of auth)
# flask_sqlalchemy
# TODO: add imports and comments
#########################

from flask import Flask, render_template, request, url_for, redirect, jsonify, send_file, session #TODO: , Blueprint
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
# Maybe figure out how to use postgres with heroku
from flask_sqlalchemy import SQLAlchemy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os, sys, plotly, json
import chart_studio.plotly as py
import plotly.graph_objects as go
import importlib
import logging
import views

###########################
### Order of operations ###
# app object constructor
# app configuration
# secret key instantiation
# login manager creation
# login manager configs
# db configuration
# centralized url routing
# logger object creation
# logger configuration
# trailing slash and space corrections
# error handling routes
# app context unit testing
# app object creation
#   db creation
#   environ config
#   app start
###########################

#TODO: move to folder riskapp, rn using just app
# riskapp = Blueprint('riskapp', __name__)
app = Flask(__name__, instance_relative_config=False)

# Define User Specific Variables - riskapp package
appName = "RiskApp Tool"

SECRET_KEY = os.environ.get('SECRET_KEY')
#TODO: temp secret key
if not SECRET_KEY:
    app.secret_key = 'secret'
    print("!!!SECRET KEY LOCALLY SET!!! ...Dev Only")

# TODO: The way i want to inject configs
# refer to app.cfg

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    # skip next for now
    if user_id is not None:
        return User.query.get(user_id)
    return None
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('unauthorized'))

# App Configs
#r = FlaskRedis()
if 'production' in os.environ:
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=14)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=300)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///memory"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initalize db
db = SQLAlchemy(app)

class Config:
     # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

class User(UserMixin, db.Model):
    """Model for user accounts."""
    __tablename__ = 'flowerShopUsers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=True)
    created = db.Column(db.String(10), nullable=True) #DateTime, unique=False, nullable=True)
    bio = db.Column(db.Text, unique=False, nullable=True)
    #admin = db.Column(db.Boolean, index=False, unique=False, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password(self.password, password)

    def validate_username(self, username):
        validUser = User.query.filter_by(username=username.data).first()
        if validUser is not None:
            error = "User is not valid"

    def validate_email(self, email):
        validEmail = User.query.filter_by(email=email.data).first()
        if validEmail is not None:
            error = "Email is not valid"

    def __repr__(self):
        return '<{},{}>'.format(self.id, self.username)

    def __init__(self, username, password, email='noEmail', created='noDate', bio='noResponse'):
        self.username = username
        self.email = email
        self.password = password
        self.created = created
        self.bio = bio

# Centralized approach - removes lazy loading, loads page as needed, cached page values
app.add_url_rule('/', view_func=views.index)
# app.add_url_rule('/login', view_func=views.login, methods=['GET','POST'])
app.add_url_rule('/hello', view_func=views.hello, methods=['GET'])
app.add_url_rule('/home', view_func=views.home)
app.add_url_rule('/generate', view_func=views.generate, methods=['POST', 'GET'])
app.add_url_rule('/contacts', view_func=views.contacts)
app.add_url_rule('/about', view_func=views.about)
app.add_url_rule('/datafunction', view_func=views.datafunction)
app.add_url_rule('/unauthorized', view_func=views.unauthorized)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userFormName = request.form['username']
        session['username'] = userFormName
        # Uses the session for username passing rather than in url or directly in html
        login_user(User.query.filter_by(username=userFormName).first())
        return redirect(url_for('home'))
    return render_template('login.html')

# app.add_url_rule('/users', view_func=views.users, methods=['GET','POST'])
@app.route('/users', methods=['GET','POST'])
def users():
    return render_template('users.html', users=User.query.all())

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            # TODO: try:
            # catch:
            users = User(request.form['username'], request.form['password'], request.form['email'])
            db.session.add(users)
            db.session.commit()
            return redirect(url_for('users'))
    return render_template('signup.html')

@app.route('/settings')
@login_required
def settings():
    return '''
        <p>Success for Settings!!!</p>
    '''

@app.route('/logout')
@login_required
def logout():
    # logout_user() # from flask_login logout_user
    session.pop('username', None)
    logout_user()
    return redirect(url_for('index'))

# create logger
#TODO: doubles out because of example.log
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# set logging file output configuration
#logger.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
# create console handler and set level to debug
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to consoleHandler
consoleHandler.setFormatter(formatter)
# add ch to logger
logger.addHandler(consoleHandler)
# log bsaic info
logger.info("Initial Startup of: " + appName)
logger.debug('This message should go to the log file')
logger.warning('Warning: Test')

# reamins here for each load - don't know if correct, but seems right
@app.before_request
def clear_trailing():
    rp = request.path
    logger.info(rp)
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# remains here for all error loading - this works!
@app.errorhandler(404)
def not_found(error):
    ##Checks to see if error is null, and catches exception
    #try:
    #    #This code may raise an error if nothing is not null
    #    error = error
    #except:
    #    error = "This is my error."
    #    app.logger.error("Application is passing null into loginerror function.")
    return render_template('notfound.html'), 404

### Unit tests ###
# For application below (unit test code coverage +70%)
# Validate that all url's are responsive and identify as themselves
with app.test_request_context('/hello', method='GET'):
    #print(url_for(''))
    assert request.path == '/hello'
    assert request.method == 'GET'

with app.test_request_context('/generate', method='POST'):
    assert request.path == '/generate'
    assert request.method == 'POST'

with app.test_request_context('/contacts'):
    assert request.path == '/contacts'

with app.test_request_context('/about'):
    assert request.path == '/about'

with app.test_request_context('/login', method='POST'):
    assert request.path == '/login'
    assert request.method == 'POST'

with app.test_request_context('/home'):
    assert request.path == '/home'

with app.test_request_context('/datafunction'):
    assert request.path == '/datafunction'
###################

#   This file is being used as both main.py and riskapp.py and some overlap in init.py
if __name__ == "__main__":
    db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
