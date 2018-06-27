
import os
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

def dbpath():
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    print("this_dir=" + this_dir)
    return os.path.join(this_dir, '..', 'database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + dbpath()
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
