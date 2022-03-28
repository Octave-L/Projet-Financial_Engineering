#!/bin/bash

FILE=.env
if [ -d "$FILE" ]; then
	echo "L'environnement virtuel $FILE existe"
else
	echo "L'environnement virtuel $FILE non existant! Création..."
	python3 -m venv $FILE
	echo "Environnement virtuel $FILE créé"
fi

source ./.env/bin/activate
pip install -r requirements.txt
python3 exercice2/main.py
deactivate
