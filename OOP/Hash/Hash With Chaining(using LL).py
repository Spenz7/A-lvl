class Node:
    def __init__ (self, data):
        self.__data = data
        self.__pointer = None

    def getData(self):
        return self.__data

    def getPointer(self):
        return self.__pointer

    def setData(self, data):
        self.__data = data

    def setPointer(self, pointer):
        self.__pointer = pointer

class LinkedList: #dynamic linked list
    def __init__(self): #Initialise method
        #dunnid Linkedlist = [Node('') for i in range(size)] as LL is dynamic
        self.__start = None

    #first type x = Linkedlist()
    #when u type print(x) u do this
##    def __str__(self): # str method, print built - in function
##        output = ''
##        temp = self.__start
##        while temp is not None:
##            output = output + "{:<10} -> ".format(temp.getData())
##            temp = temp.getPointer()
##        
##          #add None to indicate end of LL
##        output = output + "None"
##        return output

    def display(self): # Can use this function instead of the __str__ built - in function
        output = ''
        temp = self.__start
        
        while temp is not None:
            output = output + "{:<10} -> ".format(temp.getData())
            temp = temp.getPointer()
        output+=str(None)
        return output

    def addNode(self, data):
        newNode = Node(data) #grab new node !!!!! Node is the class on top !!!!!
        if self.__start is None: #empty linked list, no object in LL
            print('newNode = ',newNode)
            #self.start pts to object newNode
            self.__start = newNode
            print('self.__start = ',self.__start)
        else: #non - empty linked list
            #temp is object that was initially at the start of LL
            temp = self.__start
            self.__start = newNode # join new node at the beginning of the linked list
            newNode.setPointer(temp)

    def removeNode(self, data):
        if self.__start is not None: #non - empty linked list
            previous = None
            current = self.__start
            while current.getData() != data and current.getPointer() is not None:
                previous = current
                current = current.getPointer()
            #if find it first try
            if previous is None:
                self.__start = current.getPointer()
                print(data, "removed")
            elif current.getData() == data:
                previous.setPointer(current.getPointer())
                print(data, "removed")
            else: #data not found
                print(data, "not found. Nothing to remove.")
        else: #empty linked list
            print("No data is stored. Nothing to remove.")

    def searchNode(self, data):
        current = self.__start
        while current is not None:
            if current.getData() == data:
                return True
            current = current.getPointer()
        return False

class HashTable:
    def __init__ (self, limit = 7): #limit is the maximum number of slots
        self.__size = limit
        self.__data = [LinkedList() for i in range(self.__size)]

    def display(self):
        print("{:^5} | {}".format("Index", "Data"))
        for i in range(self.__size):
            #print(self.__data[i])
            #use line below if u use __str__ for LL cuz print(self.__data[i]) makes use of the __str__ mtd
            #print("{:^5} | {}".format(i, str(self.__data[i])))
            print("{:^5} | {}".format(i, str(self.__data[i].display())))

    def search(self, data):
        hashcode = self.hashfunction(data)
        #search that particular linked list among the array of linked lists
        thislist = self.__data[hashcode]
        if thislist.searchNode(data) == True:
            print(data, "found at index", hashcode)
        else:
            print(data, "Not found in hash table")

    def put(self, data):
        hashcode = self.hashfunction(data)
        thislist = self.__data[hashcode]
        thislist.addNode(data)


    def remove(self, data):
        hashcode = self.hashfunction(data)
        thislist = self.__data[hashcode]
        thislist.removeNode(data)

    def hashfunction(self, keydata):
        total = int(0)
        for eachchar in keydata:
            total = total + ord(eachchar)
        return total % (self.__size)
    
h = HashTable()
h.put('A5RD')
h.put('B7MF')
h.display()
            
