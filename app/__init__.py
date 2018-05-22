from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager

app = Flask(__name__)
login_manager = LoginManager()
Bootstrap(app)

from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/pcarphin/Documents/GitHub/flask_test/database.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))



