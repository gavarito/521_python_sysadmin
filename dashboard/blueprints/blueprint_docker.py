from flask import Flask, render_template, Blueprint, redirect
from docker import DockerClient

docker = Blueprint('docker', __name__, url_prefix='/docker')
con = DockerClient('tcp://192.168.0.200:2376')

@docker.route('')
def index():
    containers = con.containers.list(all=True)
    return render_template('docker.html', containers=containers)

@docker.route('/start/<shortid>')
def start_container(shortid):
    container = con.containers.get(shortid)
    container.start()
    return redirect('/docker')

@docker.route('/stop/<shortid>')
def stop_container(shortid):
    container = con.containers.get(shortid)
    container.stop()
    return redirect('/docker')