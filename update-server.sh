if ! ssh -f pi 'pushd ~/Documents/GitHub/flask_test ; ./sync-and-restart.sh' ;
then
    echo 'please make sure host named pi is defined in
    either ~/.ssh/config as in

        Host pi
            User pcarphin
            Port 22
            Hostname 123.34.56.78

'
fi
