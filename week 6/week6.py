from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

appliaction = Flask(__name__)
appliaction.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///database.db' + os.path.join(basedir,'database.db')
appliaction.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(appliaction)

class Buku(db.model):
    __tablename__ = 'tbuku'
    id = db.Column(db.String(4), primary_key=True)
    judul = db.Column(db.String(40), unique=True)
    penulis = db.Column(db.String(30))
    penerbit = db.Column(db.String(40))

    def __init__(self, id, judul, penulis, penerbit):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit

    def __repr__(self):
        return '[%s, %s, %s, %s,]' % \
               (self.id, self.judul, self.penulis, self.penerbit)