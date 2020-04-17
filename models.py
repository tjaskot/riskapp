# The import '.' tells python to look at current dir and import the relative package (example routes.py => from . import routes)
# from app import db
# from . import db
# from riskapp import db
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     email = db.Column(db.String(100), unique=True, index=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#

# from riskapp import db

class User(db.Model):
    """Model for user accounts."""
    __tablename__ = 'flowerShopUsers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=True)
    password = db.Column(db.String(50), index=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    bio = db.Column(db.Text, index=False, unique=False, nullable=True)
    #admin = db.Column(db.Boolean, index=False, unique=False, nullable=True)

    def is_authenticated(self):
        # if user is session.acive and session.auth = True:
        return self.authenticated
        # else:
        #    return self.UNauthenticated

    def __repr__(self):
        return '<{},{}>'.format(self.id, self.username)

    # Have custom init b/c don't want other info accessible
    def __init__(self, username, email, password, created, bio):
        self.username = userName
        self.email = email
        self.password = password
        self.created = created
        self.bio = bio
