#!/usr/bin/python3

import requests, json

headers = {'content-type':'application/json'}
try:
    requisicao = requests.delete('http://127.0.0.1:5000/usuarios/7', headers=headers)
    conteudo = requisicao.json()
except Exception as e:
    print('Erro: {}'.format(e))

print(conteudo)