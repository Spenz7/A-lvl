import pymongo, csv
#csv is for excel

client = pymongo.MongoClient('127.0.0.1',27017)

db = client.get_database('entertainment')
coll = db.get_collection('users')

'''
#if open file liddat then it will auto close once it reaches code not within it
#by default when open file its read mode
with open('input.txt') as csv_file:
    #basically u split using ,
    #csv.reader reads one row at a time and converts it to str and splits by ','
    csv_reader = csv.reader(csv_file,delimiter = ',')
    print(csv_reader)
    for row in csv_reader:
        coll.insert_one({'name':row[0],'age':row[1]})

#coll.find({}) returns a cursor object imagine it starts pointing
#at the first row in an excel spreadsheet        

print(coll.find({}))

for x in coll.find({}):
    print(x)

'''

#client.drop_database('entertainment')

#other way to open file   
file = open('input.txt','r')
list1 = []
for i in file:
    list1.append(i[:-1].split(','))
print(list1)

for i in list1:
    coll.insert_one({'name':i[0],'age':i[1]})
for x in coll.find({}):
    print(x)
file.close()
#client.drop_database('entertainment')


client.close()
