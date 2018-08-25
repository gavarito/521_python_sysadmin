# pip3 install jenkins

import jenkins
from pprint import pprint

try:
    con = jenkins.Jenkins('http://127.0.0.1:8080', username='gavarito', password='4linux')
except Exception as e:
    print('ERRO: {}'.format(e))
    
# Reconfigurando a job
# xml = jenkins.EMPTY_CONFIG_XML
# con.reconfig_job('4521 - exemplo', xml)

# Buscando xml de config da job
# job_xml = con.get_job_config('job-python2')
# pprint(job_xml)

#Mostrando jobs
# pprint(con.get_all_jobs())

# Buildando a job
# queue = con.build_job('4521 - exemplo')
# pprint(con.get_queue_item(queue))

# Cria uma job passando o nome e o xml
# con.create_job('4521 - exemplo', jenkins.EMPTY_CONFIG_XML)

# MOstra informações do usuario
# pprint(con.get_whoami())
# pprint(con.get_version())