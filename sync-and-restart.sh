#!/bin/bash
host_ip=$(echo $SSH_CLIENT | cut -d ' ' -f 1)
killall flask_env/bin/python
git fetch
git reset --hard origin/master
# Sync up uncommitted things
pushd app
rsync -av 'pcarphin@'$host_ip':~/Documents/GitHub/flask_test/app/*' .
popd
nohup ./run.py &
exit 0
