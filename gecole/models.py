from datetime import datetime
from gecole import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_classe = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return '<Classe {}>'.format(self.nom_classe)  

class Eleves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(20), nullable=False)
    nom = db.Column(db.String(20), nullable=False)
    classe = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return '<Eleves {}>'.format(self.classe)

  


    
