#for circular queue u need size and limit
class queue:
    def __init__(self,limit = 5):
        #limit means max 5 slots
        self.limit = limit
        self.data = [None for i in range(self.limit)]

        self.front = 0
        #rear is where u gonna insert next item
        self.rear = 0
        #size is no of occupied slots
        self.size = 0

    def display(self):
        print(self.data)
        print('Front = ',self.front)
        print('Rear = ',self.rear)
        print('Size = ',self.size)
        print('Limit = ',self.limit)

    def enqueue(self,data):
        if self.size == self.limit:
            return 'Overflow'

        #set rear to 0 to indicate that next element inserted is at index 0
        elif self.rear == self.limit-1:
            self.data[self.rear] = data
            self.rear = 0

        else:
            #rmb rear is where next item will be at
            self.data[self.rear] = data
            self.rear += 1
            
        self.size+=1

    #dequeue MUST return deleted data
    def dequeue(self):
        if self.size == 0:
            return 'underflow'
        elif self.front == self.limit-1:
            #rmb FIFO so u remove from front side
            #imagine using diagram on pg 4
            deleteddata = self.data[self.front]
            self.data[self.front] = None
            self.size -= 1
            self.front = 0
        else:
            deleteddata = self.data[self.front]
            self.data[self.front] = None
            self.size -= 1
            #only this line diff
            self.front +=1
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
x.display()
    
