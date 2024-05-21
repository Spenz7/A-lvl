from pymongo import MongoClient
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

client = MongoClient()
db = client.get_database('entertainment')
coll = db.get_collection('tv')
coll.insert_one({'name':'spencer'})
result = coll.find()
for document in result:
    print(document)
print(result.count())

db.drop_collection('tv')
for document in result:
    print(document)
print(result.count())
