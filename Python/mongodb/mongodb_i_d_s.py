from pymongo import MongoClient
from data import NOBEL_WINNERS

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

def get_mongo_database(db_name, host = 'localhost', port = 27017, username = None, password = None):
    if username and password:
        mongo_uri = 'mongodb://{user}:{pw}@{host}/{db_name}'.format(user = username, pw = password, host = host, db_name = db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]


def mongo_coll_to_dicts(dbname = 'test', collname = 'test', query = {}, del_id = True, **kw):
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))

    if del_id:
        for r in res:
            r.pop('_id')
    
    return res


db = get_mongo_database(DB_NOBEL_PRIZE)
coll = db[COLL_WINNERS]

# # insert
coll.insert(NOBEL_WINNERS)

# # delete
coll.delete_many({})

# # select
res = coll.find()
res = coll.find({'category':'Chemistry'})
res = coll.find({'year': {'$gt': 1930}})
res = coll.find({'$or' : [{'year' : {'$gt': 1930}}, {'sex': 'female'}]})
print(list(res))
# ----
print(mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS))
