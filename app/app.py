#!/usr/bin/python3

from flask import Flask, Response, jsonify
import json
from blueprints.usuarios import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/teste', methods=['GET'])
def hello ():
    # headers = {"content-type":"application/json"}
    retorno = json.dumps({
        "message":"resposta usando make_reponse"
    })
    return Response(retorno, 200, content_type="application/json")

@app.route('/exec')
def arquivo ():
    with open('nomes.txt', 'r') as arq:
        retorno = {'nomes':[x.replace('\n', '') for x in arq.readlines()]}
    return jsonify(retorno)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)