def menu():
    print('Menu')
    print('1: Insert Concert Information')
    print('2: Search for Concert Info')
    print('3: Display All Concert Info')
    print('4: Delete Concert Info')
    print('5: Exit prog')

import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database('entertainment')
coll = db.get_collection('concert')
while True:
    menu()
    option = input('Enter option')
    if option == '1':
        title = input('Title: ')
        date = input('Date:')
        time = input('Time:')
        venue = input('Venue:')
        price = input('Price:')
        try:
            #if cannot insert instead of not jumping out of prog it does except
            coll.insert_one({'title':title,'date':date,'time':time,'venue':venue,'price':price})
            print('Concert entry added')
        except:
            print('Error occurred while inserting')
            

    elif option == '2':
        title = input('enter concert title to search')
        try:
            result = coll.find({'title':title})
            if result.count() != 0:
                print('Search result:')
                for document in result:
                    print('Title',document.get('title'),'date:',document.get('date'),\
                          'time',document.get('time'),'venue:',document.get('venue'),\
                          'price:',document.get('price'))
            else:
                print('No such title')
        except:
            print('Error occurred while searching')
            
    elif option == '3':
        #result is an object that when u iterate thru it the py prog reads thru a list of dict, think of file
        result = coll.find()
        for document in result:
            print(document)
            
    elif option == '4': 
        delete = input('Enter title of concert to delete')
        try:
            result = coll.find({'title':delete})
            if result.count()!=0:
                coll.delete_one({'title':delete})
                print(delete,' is deleted')
        except:
            print('Error occurred while deleting')

    elif option == '5':
        print('Exit prog')
        break
    else:
        print('Invalid option')
    
        
        
