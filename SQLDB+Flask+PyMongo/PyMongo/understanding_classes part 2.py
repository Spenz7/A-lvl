import understanding_classes
client = understanding_classes.MongoClient('127.0.0.1',27017)
db = client.get_database('entertainent')
coll = db.get_collection('movies')
coll.insert_one({'title':'Star Wars','genre':'science fiction'})
