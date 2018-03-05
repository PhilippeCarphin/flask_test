#!flask_env/bin/python

from app import app

HOST = open('app/host.txt').readline()[:-1]

if HOST == 'localhost:5000':
    app.run(debug=True)
else:
    app.run(host='0.0.0.0')
