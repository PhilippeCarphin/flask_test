from app import app
from flask import render_template, send_from_directory, request, redirect
from app.turner import turn_file

HOST = open('app/host.txt').readline()[:-1]

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

@app.route('/server.jpg')
def server():
    return send_from_directory('..','server.jpg')


@app.route('/sgf-turner', methods=['GET', 'POST'])
def sgf_turner():
    if request.method == 'POST':

        if 'sgf-file' not in request.files:
            print(''''file' not in request.files''')
            return redirect(request.url)

        sgf_file = request.files['sgf-file']
        sgf_filename = sgf_file.filename
        turned_sgf_filename = '.'.join(sgf_filename.split('.')[:-1]) + '_turned.sgf'
        sgf_file.save(sgf_filename)
        turn_file(sgf_filename, turned_sgf_filename)
        print("SGF filename : " + turned_sgf_filename)


    return render_template('sgf-turner.html')
