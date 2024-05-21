
'''treat rear as where last item is at'''
#rear can initially pt to where last item is at OR where next item is gonna be inserted at

class queue:
    #need size and limit aka maxsize
    def __init__(self,limit):
        self.data = [None for i in range(limit)]
        
        self.front = 0
        self.rear = -1
        #to show current size
        self.size = 0
        self.limit = limit

    def enqueue(self,new):
        if self.size == self.limit:
            return 'queue overflow'
        else:
            self.size+=1
            #if at last index
            if self.rear == self.limit-1:
                self.rear = 0
                self.data[self.rear] = new
            else:
                self.rear+=1
                self.data[self.rear] = new
                
    def dequeue(self):
        #dequeue MUST return deleted data
        #always use size to check if its empty/full
        #can't if self.front == -1 to check if empty cuz u can insert some items first
        #then remove then self.front != -1 and still empty
        if self.size == 0:
            return 'queue underflow'
        else:
            deleted = self.data[self.front]
            self.data[self.front] = None
            self.size-=1
            #if at last index
            if self.front == self.limit-1:
                self.front = 0
            else:
                self.front+=1
                
        return deleted
    
    def display(self):
        print(self.data)
        print('self.front = ',self.front)
        print('self.rear = ',self.rear)
        print('self.size = ',self.size)
        print('self.limit = ',self.limit)

x = queue(5)
x.enqueue('b')
x.enqueue('c')
x.enqueue('a')
x.enqueue('x')
x.enqueue('z')
#x.display()
print(x.enqueue('y'))
x.dequeue()
x.dequeue()
x.enqueue('lol')
for i in range(5):
    print(x.dequeue())
x.enqueue('john')
x.display()
