import pymongo
import os

MONGO_URI = os.getenv('MONGO_URI')
DBS_NAME = 'myTestDb'
COLLECTION_NAME='myFirstMDB'

def mongo_connect(url):
    try:
        conn=pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('No joy ourlad: %s')% e

conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {'first': 'manuela', 'last': 'costamagna', 'dob': '06/12/1978', 'hair_color': 'red', 'nationality': 'italian', 'occupation': 'beautiful woman'}

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print (doc)