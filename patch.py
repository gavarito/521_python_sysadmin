#!/usr/bin/python3
import requests

data = {
    "nome":"joao",
    "sobrenome":"hummel"
}
requisicao = requests.patch('http://httpbin.org/patch', json=data)

conteudo = requisicao.json()
print(conteudo)