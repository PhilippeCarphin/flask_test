import os
from app import app
from flask import render_template, send_from_directory, request, redirect
from app.go_sgf_to_igo_latex.src.turner import turn_file
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from app.model import User, db

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        new_user = User(
            username=register_form.username.data,
            email=register_form.email.data,
            password=generate_password_hash(register_form.password.data, method='sha256')
        )
        db.session.add(new_user)
        db.session.commit()
        return '<H1> Registered username='+new_user.username+' email='+new_user.email+'</H1>'
    return render_template('register_page.html', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET' or not form.validate_on_submit():
        return render_template('login_page.html', form=form)
    user = User.query.filter_by(username=form.username.data).first()
    if user is None:
        return 'No user with name ' + form.username.data

    if not check_password_hash(user.password, form.password.data):
        return render_template('login_page.html', form=form, message='invalid password')

    return '<H1>' + 'Login conditions verified for user '+ form.username.data + '</H1>'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Phil'}
    return render_template('index.html')

@app.route('/english/resume_en_2018.pdf')
def resume():
    return send_from_directory('..','resume_2018_en.pdf')

@app.route('/francais/resume_fr_2018.pdf')
def resume_fr():
    return send_from_directory('..','resume_2018_fr.pdf')

@app.route('/server.jpg')
def server():
    return send_from_directory('..','server.jpg')

@app.route('/blog')
def blog():
    return render_template('blog_post.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/sgf-turner', methods=['GET', 'POST'])
def sgf_turner():
    if request.method == 'POST':

        if 'sgf-file' not in request.files:
            print('''>>>'file' not in request.files''')
            return redirect(request.url)

        sgf_file = request.files['sgf-file']
        sgf_filename = secure_filename(sgf_file.filename)

        if not sgf_filename.endswith('.sgf'):
            print('''>>> Unaccepted extension for ''' + sgf_filename)
            return error('''>>> Unaccepted extension for ''' + sgf_filename)

        print('>>> Got sgf file ' + sgf_filename)
        turned_sgf_filename = '.'.join(sgf_filename.split('.')[:-1]) + '_turned.sgf'
        sgf_file.save(sgf_filename)
        try:
            turn_file(sgf_filename, turned_sgf_filename)
        except Exception as e:
            os.rename(sgf_filename, sgf_filename + '.failed')
            print(">>> ERROR === {} === : in turn_file() for file {}{}"
                    .format(str(e), sgf_filename, '.failed'))
            return error("ERROR === {} === : in turn_file() for file {}{}"
                    .format(str(e), sgf_filename, '.failed'))

        print(">>> SUCCESS : Returning turned sgf file : " + turned_sgf_filename)
        os.remove(sgf_filename)
        ret = send_from_directory('..', turned_sgf_filename, as_attachment=True)
        os.remove(turned_sgf_filename)

        return ret

    return render_template('sgf-turner.html')

@app.route('/internal-error')
def error(message):
    return render_template('internal-error.html', message=message)