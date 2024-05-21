'''stack dunnid worry abt 1st/last time inserting/deleting, focus on stack base and stack ptr aka top ptr'''
class stack:
    def __init__(self,limit):
        self.limit = limit
        '''dunnid stackbase cuz it always starts at index 0'''
        #self.top is stacktop pts to topmost data
        self.top = -1
        self.stack = ['' for i in range(limit)]

    def push(self,data):
        if self.isfull():
            return 'full'
        self.top+=1
        self.stack[self.top] = data
        
    def pop(self):
        if self.isempty():
            return 'empty'
        deleted = self.stack[self.top]
        self.stack[self.top] = ''
        self.top-=1
        return deleted

    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top == self.limit-1

    def peek(self):
        if self.isempty():
            print('empty')
            return 
        print(self.stack[self.top])

    def display(self):
        print(self.stack)
            

x = stack(5)
x.push('a')
x.push('b')
x.push('c')
x.display()
print(x.pop())
x.display()
x.peek()
print(x.isfull())
print(x.isempty())
