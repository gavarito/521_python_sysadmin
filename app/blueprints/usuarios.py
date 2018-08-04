#!/usr/bin/python3

from flask import Flask, Blueprint, jsonify, Response, request, redirect
from bson.json_util import dumps
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

app = Flask(__name__)
usuario = Blueprint('usuario', __name__)

@usuario.route('/usuarios')
def usuarios():
    users = db.user.find()
    return Response(dumps(users), status=200, content_type="application/json")

@usuario.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    user = request.get_json()
    if user['nome'] and user['email']:
        db.user.insert_one(
        {
            "nome":user['nome'],
            "email":user['email'],
            "mensagens":user['mensagens']
        })
        mensagem = dumps({'mensagem':"Usuario {} cadastrado com sucesso".format(user['nome'])})
        status = 201    
    else:
        mensagem = dumps({'mensagem':"Informações inválidas!"})
        status = 400
    return Response(mensagem, status=status, content_type="application/json")

@usuario.route('/usuarios', methods=['PATCH'])
def atualizar_usuario():
    user = request.get_json()
    update = db.user.update_one(
        {"email":user['email']},
        {"$set":user}
    )
    if update.modified_count:
        mensagem = {"mensagem":"Usuario {} atualizado!".format(user['nome'])}
        status = 200
    elif update.matched_count:
        mensagem = {"mensagem":"Usuario {} não atualizado!".format(user['nome'])}
        status = 400
    else:
        mensagem = {"mensagem": "Usuario não encontrado!"}
        status = 404
    return Response(dumps(mensagem), status=status, content_type="application/json")

@usuario.route('/usuarios', methods=['DELETE'])
def deletar_usuario():
    user = request.get_json()
    remove = db.user.delete_one(
        {"email":user["email"]}
    )
    if remove.deleted_count:
        mensagem = {"mensagem":"Usuario {} removido com sucesso!".format(user['nome'])}
        status = 200
    else:
        mensagem = {"mensagem":"usuario não encontrado"}
        status = 404
    return Response(dumps(mensagem), status=status, content_type='application/json')

