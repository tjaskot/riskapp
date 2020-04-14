from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
# If need key value store at some point later, Redis DB:
#r = FlaskRedis()
#TODO: def create_app():

print("Reached INIT")
app = Flask(__name__, instance_relative_config=False)
#TODO: move to config.py - https://hackersandslackers.com/configure-flask-applications
#TODO: change to config file???  -  app.config['SECRET_KEY'] = 'secret'
# In config.py: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#TODO: from config.py: SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BIND
db.init_app(app)

# blueprint for auth routes in our app
#TODO: from . import riskapp as riskapp_blueprint
#TODO: remove the comment after movign files over for riskapp blueprint
# app.register_blueprint(riskapp_blueprint)

    #TODO: return app

    # Example from hks&slks
    #with app.app_context():d
    #   # Include our Routes
    #   from . import routes
    #
    #   # Register Blueprints
    #   app.register_blueprint(auth.auth_bp)
    #   app.register_blueprint(admin.admin_bp)
    #
    #   return app
