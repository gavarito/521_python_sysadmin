#!/usr/bin/python3

from flask import Flask, Blueprint, jsonify

app = Flask(__name__)
usuario = Blueprint('usuario', __name__)

def contador():
    with open('contador', 'r+') as arq:
        cont = int(arq.readline())
        cont += 1
    with open('contador', 'w') as arq:
        arq.write(str(cont))
        return cont

@usuario.route('/usuarios')
def usuarios():
    cont = contador()
    return jsonify({'status':cont})