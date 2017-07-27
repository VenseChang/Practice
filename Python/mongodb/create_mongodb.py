from pymongo import MongoClient

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

client = MongoClient()
db = client[DB_NOBEL_PRIZE]
coll = db[COLL_WINNERS]