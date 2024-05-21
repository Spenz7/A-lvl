from pymongo import MongoClient
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#return value creates instance of another class
client = MongoClient('127.0.0.1',27017)
db = client.get_database('entertainment')
coll = db.get_collection('movies')

#result is cursor object
result = coll.find()
print('all movies in collection: ')
for document in result:
    print(document)


#search query
search = {'year':{'$gt':2016}}
#update query, sets first document with year gt 2016 to 2015
update = {'$set':{'year':2015}}
#update_one uses search and update query and updates first document that matches
#the query
coll.update_one(search,update)

'''

#pg 8 q6
search = {'genre':{'$exists':False}}
update = {'$set':{'genre':'comedy'}}

coll.update_many(search,update)

result = coll.find()
print('all documents in movies collection after update_many: ')
for document in result:
    print(document)

'''

coll.update_many(search, update)
result = coll.find()
print('all documents in movies collection after update_many: ')
for document in result:
    print(document)

'''
#rmb for search query operator is second aka value
search = {'year':{'$eq':2018}}
#rmb for update its query operator first aka key
#0 means remove the field its syntax
update = {'$unset':{'year':0}}
coll.update_many(search,update)
'''

#pg 8 q7
#line below searches for all records that CONTAIN adventure genre
search = {'genre':'adventure'}
#search = {'genre':{'$eq':'adventure'}} #is the same as above
update = {'$unset':{'genre':0}}
coll.update_many(search,update)

#.find() creates cursor object
result = coll.find()
print('All documents in movies collection after unset:')
for document in result:
    print(document)

client.close()



