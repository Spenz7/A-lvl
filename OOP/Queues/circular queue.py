class queue:
    #for circular queue init self only
    def __init__(self):
        self.__data = []
        self.__limit = int(input('Size of queue?'))
        # need append dummy value if u want to start from index 1 self.__data.append('')
        
        # if u want to start from index 1: for i in range(1,self.__limit+1):
        for i in range(self.__limit):
            self.__data.append(None)
            # same as writing self.__data.append()
        
        self.__front = 0
        #self.__rear is index where u gonna insert next item
        self.__rear = 0
        self.__size = 0
        
    def display(self):
        print(self.__data)
        print('Front = ',self.__front)
        print('Rear = ',self.__rear)
        print('Size = ',self.__size)
        print('Limit = ',self.__limit)

    def enqueue(self, item):
        #insert item into queue
        #cuz eg self.__size = 7 is how many items u want to add so cuz u start from \
        #index 0 so self.__limit is 6 so u need -1
        if self.__size == self.__limit:
            return 'Queue overflow'
        #if rear is at last index u need to reset it to 0 to make way for the new data
        elif self.__rear == self.__limit-1:
            self.__data[self.__rear] = item
            self.__rear = 0
        else:
            #ur self.__rear becomes where u will insert the item after this
            self.__data[self.__rear] = item
            self.__rear += 1
            
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            return 'Queue underflow'
        #account if the front ptr is at the very last node, right before the first node so u cannot add 1 to the front ptr u need set it to 0
        elif self.__front == self.__limit-1:
            deleteddata = self.__data[self.__front]
            self.__data[self.__front] = None
            self.__size += -1
            self.__front = 0
            return deleteddata
        else:
            deleteddata = self.__data[self.__front]
            self.__data[self.__front] = None
            self.__size += -1
            self.__front+=1
            return deleteddata

x = queue()
x.enqueue('b')
x.enqueue('c')
x.enqueue('a')
x.enqueue('x')
x.enqueue('z')
print(x.enqueue('y'))
x.dequeue()
x.dequeue()
x.enqueue('lol')
for i in range(5):
    print(x.dequeue())
x.enqueue('john')
x.display()     
