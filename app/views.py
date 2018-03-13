import os
from app import app
from flask import render_template, send_from_directory, request, redirect
from app.go_sgf_to_igo_latex.src.turner import turn_file
from werkzeug.utils import secure_filename

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
