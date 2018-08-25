from flask import render_template, Blueprint, redirect, request
import jenkins as jkins

jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')
try:
    con = jkins.Jenkins('http://127.0.0.1:8080', username='gavarito', password='4linux')
except Exception as e:
    print('Erro: {}'.format(e))
    exit()


@jenkins.route('')
def index():
    jobs = con.get_all_jobs()
    return render_template('jenkins.html', jobs=jobs)

@jenkins.route('/update/<job>')
def update(job):
    job = con.get_job_name(job)
    return render_template('jenkins_update.html', job=job)

@jenkins.route('/build/<job>')
def build_job(job):
    con.build_job(job)
    return redirect('/jenkins')

@jenkins.route('/reconfig', methods=['POST'])
def reconfig():
    data = request.form
    con.reconfig_job(data['name'], data['xml'])
    return redirect('/jenkins')