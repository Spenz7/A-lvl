import pymongo
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#client is the socket
client = pymongo.MongoClient('127.0.0.1',27017)

#create database called entertainment
db = client.get_database('entertainment')

#create table called movies
coll = db.get_collection('movies')

result = coll.find()
#result is cursor object
print(result)
print('All documents in movie collection: ')
for document in result:
    print(document)
print('No of items in movie collection: ',result.count())

result = coll.find({'genre':{'$in':['adventure','comedy']}})
print('All movies w adventure/comedy genre inside: ')
for document in result:
    #don't be surprised if cursor same address for multiple objects
    print(document.get('title'))
    print(result)

query2 = {'genre':{'$exists':False}}
result = coll.find(query2)
print('all movies wo genre:')
for document in result:
    #.get returns value of title key
    print(document.get('title'))

#pg 7 q4
query3 = {'year':{'$exists':True}}
result = coll.find(query3)
print('all movies w year')
for document in result:
    yearssincerelease = 2021-document.get('year')
    print(document.get('title'),' years since release :',yearssincerelease)

result = coll.find_one({'year':{'$eq':2017}})
print('one movie that was released in 2017')
print(result)

#pg 7 q5

result = coll.find({'year':{'$lt':2017}})
print('movies released b4 2017')
for document in result:
    print(document)
client.close()
