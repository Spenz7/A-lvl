import pymongo
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

client = pymongo.MongoClient('127.0.0.1',27017)
#.database_names() returns a list of databases
#i.e since client is this python prog is like saying this py prog wants to use the method called database_names() when u type client.database_names()
databases = client.database_names()
print('databases in mongodb server are:',databases)

db = client.get_database('entertainment')

#db object has its own methods

coll = db.get_collection('movies')
#in collection u wan insert records so
#insert_one accepts a dictionary
coll.insert_one({'title':'Johnny maths','genre':'comedy'})
coll.insert_one({'title':'Star Wars','genre':'science fiction'})
coll.insert_one({'title':'Detection'}) #no genre
coll.insert_one({'title':'Detection V2'})
list_to_add = []
list_to_add.append({'title':'Batman','genre':'adventure','year':2015})
list_to_add.append({'title':'Avengers','genre':['science fiction','adventure'],'year':2017})


#insert_many accepts a list of dictionaries
coll.insert_many(list_to_add)
c = db.collection_names('entertainment')
print('Collections in entertainment database: ',c)

#client.drop_database('entertainment')




#close connection between python and mongodb server
client.close()
