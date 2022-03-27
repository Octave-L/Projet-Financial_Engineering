#!/bin/bash
FILE=.env
if [ -d "$FILE" ]; then
	echo "La machine virtuel $FILE existe"
else
	echo "Machine Virtuel non existante"
	python3 -m venv .env
fi
PATH= $( readlink -f $FILE )
source /home/octave/projet/.env/bin/activate
echo $(pwd)
python3 /home/octave/projet/exercice2/main.py
