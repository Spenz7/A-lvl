import pymongo,json
client = pymongo.MongoClient('127.0.0.1',27017)
#print(client.get_database())
#same as get_database and get_collection
db = client['entertainment']
coll = db['moreusers']

with open('input.json') as file:
    data = json.load(file)
    #data is list of dict, basically copying text from json file into a straight line
    print(data)
#line below is same as documented code
#when first run line below if dh database/collection it creates it
#client['entertainment']['moreusers'] is same as coll
client['entertainment']['moreusers'].insert_many(data)
for x in client['entertainment']['moreusers'].find({}):
    print(x)

#above is good to know just stick to method below

'''
file = open('input.json','r')
data = json.load(file)
print('data = ',data)
db = client.get_database('entertainment')
coll = db.get_collection('moreusers')
coll.insert_many(data)
for x in coll.find({}):
    print(x)
#client.drop_database('entertainment')
file.close()
'''

client.close()
