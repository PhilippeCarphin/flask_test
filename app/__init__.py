from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
Bootstrap(app)

from app import views

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/pcarphin/Documents/GitHub/flask_test/database.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)


@app.route('/testlogin')
def test_login():
    result = User.query.filter_by(username='Phil')
    print(result)
    user = result.first()

    if user is None:
        return 'No user named Phil'
    print(user)
    return '<H1>' + 'There is a user with username=Phil with id=' + str(user.id) + '</H1>'

