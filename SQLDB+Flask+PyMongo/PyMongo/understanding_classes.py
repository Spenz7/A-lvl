#connect python to mongodb server
#pymongo is like a module(file) containing classes such as MongoClient
#so line of code below means u use the pymongo module and use a class in that module and
#u initialise an object from the MongoClient class thats y the info within ()
#is used to initialise a MongoClient object thus creating an instance of the
#MongoClient class called client so u can use methods under the MongoClient class
class MongoClient:

    def __init__(self,ip,port_no):
        self.ip = ip
        self.port_no = port_no
        
    def get_database(self,database_name):
        return database(database_name)

class database:
    def __init__(self,database_name):
        self.database_name =  database_name

    def get_collection(self,collection_name):
        return collection(collection_name)

class collection:
    def __init__(self,collection_name):
        self.collection_name = collection_name
        self.collection = []
        
    def insert_one(self,dictionary):
        self.collection.append(dictionary)
        print(self.collection)
        


