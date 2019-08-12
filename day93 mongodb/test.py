from pymongo import MongoClient

MC = MongoClient(host='127.0.0.1', port=27017)

# MG = MC['day93']
# # res = mongo.users.insert_one({'name':'iris'})
# # print(res, type(res.inserted_id))
# # res = mongo.users.find({'name': 'henry'})
# # print(list(res), type(res))
# # res = mongo.users.find({'_id':ObjectId('5d513e0a0d3a3d6dd9a19101')})
# # print(list(res))
# # res = mongo.users.insert_one({'name':'echo'})
# count = 2
# # res = mongo.users.find({}).sort({'age': 1}).limit(2)
# from pymongo import ASCENDING
# res = MG.users.find().limit(2).sort('age',ASCENDING)
# for row in res:
#     print (row)

mongo = MC['game']
res = mongo.players.find()
print(list(res)[0])