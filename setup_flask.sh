#!/bin/sh
###############################################################################
# Setup variables
###############################################################################
VENV=flask_env
PYTHON=python3
PACKAGES="flask cock bitcoin"

BIN=$VENV/bin
PIP=$BIN/pip


# REFERENCE
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

eval_or_print()
{
	cmd="$@"
	if [[ $just_print == true ]] ; then
		echo "$cmd"
	else
		eval "$cmd"
	fi
}



just_print=false
while [[ $# -gt 0 ]] ; do
	opt=$1
	arg=$2
	case $opt in
		--just-print)
			just_print=true
			;;
		--add-package)
			eval_or_print $PIP install $arg
			echo $0
			if [[ $? == 0 ]] ; then
				echo "eval_or_print \$PIP install $arg" >> $0
			fi
			exit 0
			;;
	esac
	shift
done

set -o xtrace
eval_or_print $PYTHON -m venv $VENV
for pack in $PACKAGES ; do
	eval_or_print $PIP install $pack
done
eval_or_print $PIP install flask-wtf
