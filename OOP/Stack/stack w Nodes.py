
class node:
    def __init__(self,data = None):
        self.__data = data

    def setdata(self,data):
        self.__data = data
    def getdata(self):
        return str(self.__data)

class stack:
    def __init__(self,size = 5):
        self.__stack = [node() for i in range(5)]
        self.__top = 0
        self.__size = size

    def insert(self,item = None):
        if item == None or type(item) != str:
            item = str(input("Item to be inserted: "))

        if self.__top == self.__size:
            return "Stack is full"

        self.__stack[self.__top].setdata(item)
        self.__top += 1
        return f"{item} has been inserted"

    def delete(self):
        if self.__top == 0:
            return "Stack is empty"
        self.__top -= 1
        item = self.__stack[self.__top].getdata()
        self.__stack[self.__top].setdata(None)
        return f"{item} has been removed"

    def display(self):
        print(f"{'Index':^5}|{'Data':^16}")
        for i in range(self.__size):
            print(f"{i:^5}|{self.__stack[i].getdata():^16}")

        print(f"Size: {self.__size}")

x = stack()
x.display()
x.insert('A')
x.insert('B')
x.display()
x.delete()
x.display()
