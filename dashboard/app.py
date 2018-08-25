from flask import Flask, render_template, Blueprint
from blueprints.blueprint_docker import docker
from blueprints.bjenkins import jenkins

app = Flask(__name__)
app.register_blueprint(docker)
app.register_blueprint(jenkins)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)