'''must insert into coll b4 database can be shown'''
import pymongo
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
client = pymongo.MongoClient('localhost',27017)
#client.drop_database('test')
db = client.get_database('testdb')
coll = db.get_collection('testcoll')




'''INSERTING'''
#coll.insert_one({'name':'spencer'})

#if wan multiple values per cell use a list
#coll.insert_one({'name':['A','B']})

import json
records = []
file = open('input.json','r')
x = json.load(file)
for i in x:
    #i is a dict
    records.append(i)
print(records)
file.close()
#coll.insert_many(records)

'''DISPLAYING'''
dbnames = client.database_names()
print(dbnames)

collnames = db.collection_names('test.db')
print(collnames)

'''unique id'''
#by default {'_id': ObjectId('6157fb9a0c60b5be96a36444'), 'name': 'spencer'}
#if u wan a a unique record use _id that replaces ObjectId
#coll.insert_one({'_id':1,'name':'chelsea'})

'''multiple values per cell(value) '''

'''others'''
#imagine cursor at top of table
cursor = coll.find()
print(cursor)
for i in cursor:
    print(i)
print(coll.count())

'''queries'''
#query = {'query operator':list(info that u wan in dict)}
#coll.insert_one({'name':'spencer','year':2021})
query = {'name':'spencer','year':{'$gt':2016}}

result = coll.find(query)
print(result)
for i in result:
    print(i)

'''update'''
#mtds all take in dict
search = {'year':{'$gt':2016}}
update = {'$set':{'year':2020}}
coll.update_one(search,update)

result = coll.find(query)
for i in result:
    print(i)

search = {'name':'spencer7'}
update = {'$set':{'name':0}}
coll.update_many(search,update)
result = coll.find({'name':0})
for i in result:
    print(i)
client.close()



