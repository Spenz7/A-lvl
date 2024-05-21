#run py prog 2 from pg 2 b4 running this
import pymongo
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database('entertainment')
coll = db.get_collection('movies')

'''
#.find() by default is .find({}) which means find all
result = coll.find()
#result is a cursor object pointing at the document
print('All documents in movie collection:')
for document in result:
    #for each time u iterate thru this the cursor moves to a new record
    #imagine cursor moving down a table
    print(document)
print('Number of items in movie collection:',coll.count())

result = coll.find({'genre':'adventure'})
print('All movies with adventure genre:')
for document in result:
    print(document)
'''

#pg 5
#RMB {'query operator':info that u want}
#for and operator
##query2 = {'$and':[{'genre':'adventure'},{'year':{'$gt':2016}}]}
    
#for or operator
query2 = {'$or':[{'genre':'adventure'},{'year':{'$gt':2016}}]}

#this is simplified ver of AND query so must be adventure genre and
#year greater than 2016
#query2 ={'genre':'adventure','year':{'$gt':2016}} 
result = coll.find(query2)
print('All titles of movies with adventure genre after 2016:')
for document in result:
    #.get('title') is a built-in dic func that i.e returns value cuz 'title'
    #is the key 
    print('-'+document.get('title'))
print('There are ',result.count(),'movies in the list above')
client.close()
