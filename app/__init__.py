from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
Bootstrap(app)

from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/pcarphin/Documents/GitHub/flask_test/database.db'
app.config['SECRET_KEY'] = 'thisissecret'

login_manager.init_app(app)





