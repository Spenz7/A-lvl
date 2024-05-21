class Node:
  def __init__(self,name,pointer=-1):
    self.__name = name
    self.__pointer = pointer
  def getname(self):
    return self.__name
  def getpointer(self):
    return self.__pointer
  def setname(self,name):
    self.__name = name
  def setpointer(self,pointer):
    self.__pointer = pointer
class linkedlist:
  def __init__(self,size):
    self.__list = [Node('') for i in range(size)]
    for i in range(len(self.__list)-1):
      self.__list[i].setpointer(i+1)
    self.__start = -1
    self.__nextfree = 0

  def display(self):
    print('self.__start=',self.__start)
    print('self.__nextfree',self.__nextfree)
    print('{0:^5}|{1:^10}|{2:^10}'.format('Index','Name','Pointer'))
    for i in range(len(self.__list)):
      print('{0:^5}|{1:^10}|{2:^10}'.format(i,self.__list[i].getname(),self.__list[i].getpointer()))

  def insert(self,newname):
    if self.__nextfree == -1:
      print('No free node')
      return False
    
    self.__list[self.__nextfree].setname(newname)

    if self.__start == -1:
      temp  = self.__list[self.__nextfree].getpointer()
      self.__list[self.__nextfree].setpointer(-1)
      self.__start = self.__nextfree
      self.__nextfree = temp
    
    else:
      current = self.__start
      previous = -1
      while current !=-1:
        if newname<self.__list[current].getname():
          break
        previous = current
        current = self.__list[current].getpointer()
      if previous == -1:
        temp  = self.__list[self.__nextfree].getpointer()
        self.__list[self.__nextfree].setpointer(self.__start)
        self.__start = self.__nextfree
        self.__nextfree = temp
      else:
        temp  = self.__list[self.__nextfree].getpointer()
        self.__list[self.__nextfree].setpointer(current)
        self.__list[previous].setpointer(self.__nextfree)
        self.__nextfree = temp


  def delete(self,data):
    if self.__start == -1:
      print('Empty list')
      return False
    current = self.__start
    previous = -1
    while current!=-1:
      if data == self.__list[current].getname():
        self.__list[current].setname('')
        break
      previous = current
      current = self.__list[current].getpointer()
    if current == -1:
      print('{} not found in list'.format(data))
      return False
    # only step 3 differs for if and else
    if previous == -1:
      temp = self.__nextfree
      self.__nextfree = current
      self.__start = self.__list[current].getpointer()
      self.__list[current].setpointer(temp)
    else:
      temp = self.__nextfree
      self.__nextfree = current
      self.__list[previous].setpointer(self.__list[current].getpointer())
      self.__list[current].setpointer(temp)

  def search(self,data):
    current = self.__start
    while current !=-1 and self.__list[current].getname()<=data:
      if self.__list[current].getname()==data:
        print('{} found at index {}'.format(data,current))
        return
      current = self.__list[current].getpointer()
    print('{} not found in linked list'.format(data))



  def printinorder(self):
    if self.__start!=-1:
      print('Printing in alphabetical order')
      current = self.__start
      while current!=-1:
        print(self.__list[current].getname())
        current = self.__list[current].getpointer()
    else:
      print('No data exists in linked list')

def menu():
  print('''
  1. Initialise linked list
  2. Insert item
  3. Delete item
  4. Display linked list
  5. Search item
  6. Print in alphabetical order
  ''')

def main():
  menu()
  linkedlistexist = False
  choice = input('enter your choice')
  while choice!='7':
    if choice == '1':
      LL = linkedlist(8)
      print('Initialising 8 nodes')
      linkedlistexist = True
    elif choice == '2':
      if linkedlistexist == False:
        print('No linked list exists')
      else:
        newname = input('Enter item to insert')
        if LL.insert(newname)!=False:
          print('{} inserted'.format(newname))
    elif choice == '3':
      if linkedlistexist == False:
        print('No linked list exists')
      else:
        name = input('Enter item to delete')
        if LL.delete(name)!=False:
          print('{} deleted'.format(name))
    elif choice == '4':
      if linkedlistexist == False:
        print('No linked list exists')
      else:
        LL.display()
    elif choice == '5':
      if linkedlistexist == False:
        print('No linked list exists')
      else:
        data = input('Enter item to search')
        LL.search(data)
    elif choice == '6':
      if linkedlistexist == False:
        print('No linked list exists')
      else:
        LL.printinorder()
    else:
      print('Wrong option entered')
    
    menu()
    choice = input('enter your choice')
  print('exit program')
main()

