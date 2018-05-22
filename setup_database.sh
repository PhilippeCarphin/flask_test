#!/bin/bash

echo "$(tput setaf 3)PHIL: I entered .tables, it showed nothing but then CTRL-D
and there is a *.db file now.$(tput sgr 0)"
sqlite3 database.db

echo "$(tput setaf 3)PHIL: other stuff to do with the database, type
In the python REPL, do the two commands:
from app import db
db.create_all()$(tput sgr 0)"
./flask_env/bin/python

echo "$(tput setaf 2)PHIL: If there are no errors after db.create_all(),
then in sqlite3, you can do
.tables
and you should see 'user'$(tput sgr 0)"
sqlite3 database.db

echo "$(tput setaf 3)PHIL: To test, go to '/register', enter valid stuff, and
click register.  You should be able to go into sqlite3 and see that data when
you do
select * from user;$(tput sgr 0)"
sqlite3 database.db
