#read notes as u go along
import pymongo
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database('entertainment')

#database_names() returns a list 
dbnames = client.database_names()
print('dbnames = ',dbnames)

coll = db.get_collection('actor')

#try commenting out the line below and run prog again to re-add 'actor'
#db.drop_collection('actor')
#line below returns list of collection names in db called entertainment

collnames = db.collection_names('entertainment')

print('collname = ',collnames)
coll.insert_one({'James bond':'age 20'})
#if u want sth to be unique use '_id:1' which means that this record has a unique id of 1, if dw unique just remove the _, _ only works for id
#col.insert_one({'_id':2,'Donny yen':'age 50'})
insertlist = []
insertlist.append({'Chris evans':'age 30'})
#key or value must be atomic so if wan include multiple values use a list
insertlist.append({'Tony stark':['age 40','sex M']})
#insert_many parameter is list of dictionaries
coll.insert_many(insertlist)

#to print out every document(record)
#result is a cursor object imagine it starts at top of table
result = coll.find()
for document in coll.find():
    print(document)

#see prog in pg5 of notes, prog 4

#to count no. of records
print(coll.count())



#use this if u want to remove a database rmb client.
#try running prog without line of code below and then add line of code below
#and then only run till print dbnames shd show entertainment being removed
#client.drop_database('entertainment')

#if u do this below u can't view it bcuz u haven't inserted anything into it yet
#see pg 2 of notes highlighted part
db = client.get_database('school')
    

#MUST CLOSE 
client.close()

#see pg 4 prog 3
#see pg 7 prog 6
