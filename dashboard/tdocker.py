#pip3 install docker
import docker

try:
    con = docker.DockerClient('tcp://192.168.0.200:2376')
except Exception as e:
    print('Erro: {}'.format(e))

# container = con.containers.run(
#     'debian','/bin/bash',
#     name='imagepython', detach=True,
#     tty=True, ports={'5000/tcp':'5000'}
# )

# print(container.id, container.image.tags[0], container.name, container.short_id, container.status)

# containers = con.containers.list(all=True)

# ids = [x.short_id for x in containers]
# print(ids)

# for container in containers:
#     print(container.name, container.status, sep=':')

# container = con.containers.get('f8d6520db942')
# print(container.name, container.short_id)

# container = con.containers.get('f8d6520db942')
# container.stop()
# container.start()
# container.stats(stream=False)
# container.attach()
# container.remove()
containers = con.containers.list(all=True)
for container in containers:
    container.start()