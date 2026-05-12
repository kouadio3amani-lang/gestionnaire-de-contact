from web.__init__ import db
from flask_login import UserMixin
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nom = db.Column(db.String(150))
    email = db.Column(db.String(150))
    telephone = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    nom = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    mdp = db.Column(db.String(150))
    Contacts = db.relationship('Contact', lazy=True)



    
