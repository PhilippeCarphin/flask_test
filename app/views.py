from app import app
from flask import render_template, send_from_directory

HOST = 'localhost:5000'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Phil'}
    return render_template('index.html', host=HOST)

@app.route('/english/resume_en_2018.pdf')
def resume():
    return send_from_directory('..','resume_2018_en.pdf')

@app.route('/francais/resume_fr_2018.pdf')
def resume_fr():
    return send_from_directory('..','resume_2018_fr.pdf')
