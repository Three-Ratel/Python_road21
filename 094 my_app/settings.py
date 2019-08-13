from pymongo import MongoClient

MG = MongoClient('127.0.0.1', 27017)
mongo = MG['MyApp']
