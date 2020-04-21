# ### config.py ###
# from os import environ
#
# class Config:
#     """Set Flask configuration vars from .env file."""
#
#     # General
#     TESTING = environ.get('TESTING')
#     FLASK_DEBUG = environ.get('FLASK_DEBUG')
#     SECRET_KEY = environ.get('SECRET_KEY')
#
#     # Database
#     SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
#
# ### Copied Code ###
# #base directory for sqlalchemy database file
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# class Config(object):
#     # ...
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
# from app import routes, models
#
# ### app/models.py ###
# from datetime import datetime
# from app import db
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
#
# print("REACHED CONFIG")
