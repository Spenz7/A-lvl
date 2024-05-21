
#for alphabets
#this is used to generate org index for data that pt to same index
def hashfn(value,size):
    total = 0 
    #add up add the ascii value of all the characters
    for i in value:
        total += ord(i)
    #index is hash value
    index  = total%size
    return index
    

##print(array)
##
###hashvalue = hashfn(x,len(array))
##print('hashvalue = ',hashvalue)
##array[hashvalue] = x
##print(array)


#array is array to be inserted in
#x is the alphabetical string that u want to insert
def insert(x,array):
    hashvalue = hashfn(x,len(array))
    if array[hashvalue] == '':
        array[hashvalue] = x
        print(array)
        
        return hashvalue
    else:
        #marker to indicate when u reach back to starting pt
        originalhashvalue = hashvalue
        while array[hashvalue] != '':
            #if reach last index 
            if hashvalue == len(array)-1:
               hashvalue = 0
            #if haven't reach the end yet
            elif hashvalue!= len(array)-1:
                hashvalue+=1
            elif hashvalue == originalhashvalue:
                return 'No empty space'

        
        array[hashvalue] = x
        print(array)
        
        return hashvalue
        

#array is array to search in
def search(searchvalue,array):
    hashvalue = hashfn(searchvalue,len(array))
    while True:
        if array[hashvalue] == searchvalue:
            global finalhashvalue
            finalhashvalue = hashvalue
            return '{} found at index: {}'.format(searchvalue,hashvalue)
        elif array[hashvalue] == '':
            return('not found')
            
        #if reach last index
        elif hashvalue == len(array)-1:
           hashvalue = 0
        #if haven't reach the end yet
        elif hashvalue!= len(array)-1:
            hashvalue+=1    
        elif hashvalue == originalhashvalue:
            return('not found')
                
        
        
array = ['' for i in range(97)]
inputlist = ['A5RD','M7DE','B7MF','GQ4B']
for i in inputlist:
    print(insert(i,array))
x = search('B7MF',array)
print(x)


def delete(deletevalue,array):
    if search(deletevalue,array) == 'Not found':
        return 'not found'
    else:
        
        #x to mark tombstone
        array[finalhashvalue] = 'X'

delete('GQ4B',array)
print(array)
