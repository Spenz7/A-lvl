#FIFO
#linear queue
#rear is where last element is at
class queue:
    def __init__(self):
        self.arr = [None for i in range(3)]
        self.size = len(self.arr)
        #queue itself has a front and rear of -1
        self.front = -1
        self.rear = -1

    def enqueue(self,new):
        #rear is where lastest item is at
        if self.rear == self.size-1:
            print('full')
        else:
            if self.front == -1:
                self.front+=1
            self.rear +=1
            self.arr[self.rear] = new
               
    def dequeue(self):
        if self.front<0 or self.front>self.size-1 :
            print('empty')
        else:
            self.arr[self.front] = ''
            self.front+=1

    def display(self):
        print(self.arr)
        print('self.front = ',self.front)
        print('self.rear = ',self.rear)

x = queue()
x.enqueue('A')
x.enqueue('B')
x.enqueue('C')
x.display()
x.enqueue('D')
x.dequeue()
x.dequeue()
x.dequeue()
x.dequeue()
x.display()     




