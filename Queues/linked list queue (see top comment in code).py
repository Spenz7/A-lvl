#only diff btwn linkedlist and linear is that linkedlist
#u can reuse the node that u dequeued the value from as a free node
#and setting that node as the very first free node available
#while for linear queue u can't reuse the node that u deleted the data from
class Node:
    def __init__(self, data):
        self.__data = data
        self.__ptr = -1
    def getData(self):
        return self.__data
    def setData(self,data):
        self.__data = data
    def getptr(self):
        return self.__ptr
    def setptr(self,ptr):
        self.__ptr = ptr

class Queue:
    def __init__(self,limit):
        self.__data = [Node('') for i in range(limit)]
        for i in range(len(self.__data)-1):
            self.__data[i].setptr(i+1) #last node still has ptr to -1
        self.__limit = limit
        self.__front = -1
        self.__size = 0
        self.__nextfree = 0
        #self.__rear = 0
    def display(self):
        for i in range(len(self.__data)):
            print('{:^5}|{:^10}|{:^10}'.format(i, self.__data[i].getData(),self.__data[i].getptr()))
        print('Front =',self.__front)
        print('Size =',self.__size)
        print('Limit =',self.__limit)
        print('Nextfree=',self.__nextfree)
    def enqueue(self,item):
        if self.__nextfree == -1:
            return 'Queue overflow'
        p = self.__front
        
        #if first time inserting, then p = -1, and self.__data[p]
        #is self.__data[-1] which is the last node of the queue
        #print(self.__data[p].getptr())
        while self.__data[p].getptr() != -1:
            p = self.__data[p].getptr()
            
        self.__data[self.__nextfree].setData(item)
        temp = self.__data[self.__nextfree].getptr()
        self.__data[self.__nextfree].setptr(-1)
        #must have this if statement cuz if go to the else statement then u
        #change the ptr of the last node to the very first node then
        #there's no end to the queue
        if self.__front == -1:
            self.__front = self.__nextfree
        else:
            #i.e p pts to the initial latest node
            self.__data[p].setptr(self.__nextfree)
        self.__nextfree = temp
        self.__size += 1

    def dequeue(self):
        
        if self.__front == -1:
            return 'Queue underflow'
        dequeueditem = self.__data[self.__front].getData()
        temp = self.__front
        self.__data[self.__front].setData('')
        self.__front = self.__data[self.__front].getptr()
        self.__data[temp].setptr(self.__nextfree)
        self.__nextfree = temp
        self.__size += -1
        return dequeueditem

x = Queue(5)
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
    
