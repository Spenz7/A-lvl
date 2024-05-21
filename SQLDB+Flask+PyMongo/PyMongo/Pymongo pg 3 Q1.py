import pymongo
title  = input('Enter movie title: ')
year = input('Enter year of movie: ')
client = pymongo.MongoClient('127.0.0.1',27017)
#to create a database u must create an instance of the MongoClient class
db = client.get_database('entertainment')
#to use get_collection u must create an instance of another class
coll = db.get_collection('movies')
coll.insert_one(('title':title,'year':year))
client.close()
