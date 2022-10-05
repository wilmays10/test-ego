#!/bin/bash

# entorno virtual
sudo apt update
sudo apt install python3-pip
python3 -m venv env
source env/bin/activate

# instalar dependencias
pip3 install -r requirements.txt

# Inicializar server local
python manage.py runserver