#!/bin/bash
pushd ~/Documents/GitHub/flask_test
killall flask_env/bin/python
git fetch
git reset --hard origin/master
# Sync up uncommitted things
pushd app
rsync -av 'pcarphin@192.168.2.15:~/Documents/GitHub/flask_test/app/*' .
popd
nohup ./run.py &

