#!/usr/bin/python3

from ldap3 import Server, Connection
from hashlib import md5
from binascii import b2a_base64

try:
    server = Server('ldap://127.0.0.1:389')
    con = Connection(
        server,
        "cn=admin,dc=dexter,dc=com,dc=br", password='4linux'
    )
    con.bind()
    md5json = md5('senhapadrao'.encode('utf-8')).digest()
    user = {
        'cn': 'joao',
        'sn': 'hummel',
        'mail': 'joao.hummel@4linux.com.br',
        'uidNumber': '123',
        'gidNumber': '123',
        'uid': 'joao',
        'homeDirectory': '/home/joao',
        'userPassword': "{}"+b2a_base64(md5json).decode('utf-8')
    }
    objectClass = ['top', 'person', 'organizationalPerson', 'inetOrgPerson', 'posixAccount']
    cn='uid='+user['mail']+',dc=dexter,dc=com,dc=br'
    print(con.add(cn, objectClass, user)) 
    # email = 'joseph.santos@4linux.com.br'
    # dn = "uid=joseph.santos,dc=dexter,dc=com,dc=br"
    # con.search(
    #     dn, '(objectclass=person)',
    #     attributes=['sn', 'userPassword']
    # )
    # print(con.entries)
except Exception as e:
    print('Erro: {}'.format(e))