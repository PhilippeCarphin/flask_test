#!/bin/sh

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

VENV=flask_env
PYTHON=python3
BIN=$VENV/bin
PIP=$BIN/pip

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

eval_or_print $PYTHON -m venv $VENV
eval_or_print $PIP install flask
