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
sqlite3

echo "$(tput setaf 3)PHIL: In order to user the /testlogin route,
do this in the python REPL:
from app import db, User
phil = User(username='Phil')
db.session.add(phil)
db.session.commit()
res = User.query.all()
res[0].username$(tput sgr 0)"
./flask_env/bin/python
echo "$(tput setaf 2)You should see 'Phil' and if you go to the /testlogin page,
you should now see 'There is a user with username=Phil'.$(tput sgr 0)"
