from pymongo import MongoClient, ASCENDING
from bson import ObjectId
MC = MongoClient(host='127.0.0.1', port=27017)

MG = MC['day93']
# res = MG.users.insert_one({'name':'iris', 'age':19})
# print(res, type(res.inserted_id))
# res = MG.users.find({'name': 'iris', 'age':19})
# # print(list(res), type(res))
# res = MG.users.find({'_id': ObjectId('5d51fd29c128f4b1b69af11c')})
# print(list(res))
# res = mongo.users.insert_one({'name':'echo'})
# count = 2
# res = mongo.users.find({}).sort({'age': 1}).limit(2)
# from pymongo import ASCENDING


# mongo = MC['game']
# res = mongo.players.find()
# print(list(res)[0])
