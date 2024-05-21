#def nodes
class node:
    def __init__(self, data = ''):
        self.__data = data
        self.__ptr = -1
    def getdata(self):
        return self.__data
    def setdata(self,data):
        self.__data = data
    def getptr(self):
        return self.__ptr
    def setptr(self,ptr):
        self.__ptr = ptr
        
class queue:
    def __init__(self,limit = 5):
        self.data = [node() for i in range(limit)]
        
        self.limit = limit
        #last node dunnid
        for i in range(self.limit-1):
            self.data[i].setptr(i+1)
        
        self.front = -1
        self.size = 0
        self.nextfree = 0
        #only diff from normal LL is self.front cuz u need it to know
        #what to dequeue
        

    def enqueue(self,data):
        #check for overflow
        if self.nextfree == -1:
            return 'overflow'
        
        current = self.front
        #loop till u find last occupied node
        while self.data[current].getptr() != -1:
            current = self.data[current].getptr()

        self.data[self.nextfree].setdata(data)
        temp = self.data[self.nextfree].getptr()
        self.data[self.nextfree].setptr(-1)
        #if first time inserting
        if self.front == -1:
            self.front = self.nextfree
        else:
            #p is last occupied node
            self.data[current].setptr(self.nextfree)
        self.nextfree = temp
        self.size += 1

    def dequeue(self):
        if self.front == -1:
            return 'underflow'
        dequeueditem = self.data[self.front].getdata()
        temp = self.front
        self.data[self.front].setdata('')
        self.front = self.data[self.front].getptr()
        self.data[temp].setptr(self.nextfree)
        self.nextfree = temp
        self.size-= 1
        return dequeueditem
    
    def display(self):
        for i in range(len(self.data)):
            print('{:^5}|{:^10}|{:^10}'.format(i,self.data[i].getdata(),self.data[i].getptr()))
        print('Front =',self.front)
        print('Size =',self.size)
        print('Limit =',self.limit)
        print('Nextfree=',self.nextfree)
x = queue()
x.enqueue('b')
x.enqueue('c')
x.enqueue('a')
x.enqueue('x')
x.enqueue('z')
x.display()
print(x.enqueue('y'))
x.dequeue()
x.dequeue()
x.enqueue('lol')
x.display()
for i in range(5):
    print(x.dequeue())
x.display()
