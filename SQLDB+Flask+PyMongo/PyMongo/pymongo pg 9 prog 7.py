from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)
db = client.get_database('entertainment')
coll = db.get_collection('movies')

list1 = []
list1.append({'year':2015})
list1.append({'year':2015,'name':'spencer'})
coll.insert_many(list1)

result = coll.find()
print('all documents in collection: ')
for document in result:
    print(document)

'''
#deletes first document that has year 2015
coll.delete_one({'year':2015})
print('all documents in collection after delete_one: ')
result = coll.find()
for document in result:
    print(document)
'''

coll.delete_many({'year':2015})
#q8
#coll.delete_many({'genre':'adventure'})

print('all documents in collection after delete_many: ')
result = coll.find()
for document in result:
    print(document)
