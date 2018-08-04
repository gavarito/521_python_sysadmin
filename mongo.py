#!/usr/bin/python3

from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

user = db.user.update_one(
    {"_id":ObjectId("5b65b1b8e3d0b512a6e494af")},
    {
        "$pull":{
            "mensagens":{
                "nome":"joseph"
        }
    }}
)
print(user.matched_count, user.modified_count)

# user = db.user.update_one(
#     {"mensagens.nome":"novousuario"},
#     {
#         "$set":{
#             "mensagens.$.nome":"joseph"
#         }
#     }
# )

# user = db.user.update_one(
#     {"_id":ObjectId("5b65b1b8e3d0b512a6e494af")},
#     {
#         "$push":{
#             "mensagens":{
#                 "nome":"novousuario",
#                 "mensagem":"novamensagem"}
#         }
#     }
# )


# user= db.user.delete_one(
#     {"_id":ObjectId("5b65a4bfe3d0b50d5b718c0a")}
# )
# print(user.deleted_count)

# print(db.user.find_one({"_id":ObjectId("5b65a4bfe3d0b50d5b718c0a")}))

# user = db.user.update_one(
#     {"nome":"joseph santos"},
#     {"$set":{
#         "email":"joseph.santos@yahoo.com"
#     }}
# )
# print(user.matched_count, user.modified_count)

# users = [x for x in db.user.find({'nome':'joseph santos'})]

# for u in user:
# print(users)

# print(user)
# print(user["_id"].generation_time)

# db.user.insert_one(
#     {
#         "nome":"joseph santos",
#         "email":"joseph.santos@gmail.com",
#         "mensagens":[
#             {
#                 "nome":"usuario",
#                 "mensagem":"mensagem"
#             }
#         ]
#     }
# )