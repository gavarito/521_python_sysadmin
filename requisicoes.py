#!/usr/bin/python3

import requests, json

headers = {'content-type':'application/json'}
data = json.dumps({
    "nome":"gavarito2",
    "email":"gavarito2@gmail.com"
})

try:
    requisicao = requests.post('http://127.0.0.1:5000/usuarios', data=data, headers=headers)
    conteudo = requisicao.json()
except Exception as e:
    print('Erro: {}'.format(e))

print(conteudo)