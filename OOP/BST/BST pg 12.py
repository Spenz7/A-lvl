nullpointer = 0
class TreeNode:
    def __init__(self,data,left=0,right=0):
        self.__data = data
        self.__left = left
        self.__right = right

    def getdata(self):
        return self.__data
    def getleft(self):
        return self.__left
    def getright(self):
        return self.__right
    def setdata(self,data):
        self.__data = data
    def setleft(self,left):
        self.__left = left
    def setright(self,right):
        self.__right = right

class BST:
    def __init__(self,size=7):
        self.__tree = [None] + [TreeNode('') for i in range(size)]
        for i in range(1,size):
            #point to next node
            self.__tree[i].setleft(i+1)
        #set last node left ptr to null
        self.__tree[size].setleft(nullpointer)
        self.__rootptr = nullpointer
        self.__freeptr = 1
        self.__size = size

    def display(self):
        print('{:5}|{:^5}|{:^10}|{:^5}'.format('Index','Left','Data','Right'))
        for i in range(1, self.__size+1):
            print('{:5}|{:^5}|{:^10}|{:^5}'.format(i,self.__tree[i].getleft(),\
                                                   self.__tree[i].getdata(),\
                                                   self.__tree[i].getright()))
        print('Root ptr = ',self.__rootptr)
        print('Free Ptr = ',self.__freeptr)

    def insert(self,newitem):
        #see pg 12 of notes
        #when there is space and u insert data into an empty/nonempty tree u still need to put the data in regardless
        #i.e this if statement is the common factor of the nested if/else statements below
        '''Whenever insert data first set its ptrs to null'''
        if self.__freeptr != nullpointer:
            newnodeptr = self.__freeptr
            self.__freeptr = self.__tree[self.__freeptr].getleft()
            self.__tree[newnodeptr].setdata(newitem)
            #set left and right to null cuz its a leaf node
            self.__tree[newnodeptr].setleft(nullpointer)
            #print(self.__tree[newnodeptr].getleft())
            self.__tree[newnodeptr].setright(nullpointer)

            
            #after inserting data u check if tree is empty (i.e u insert data for the first time)
            #rootptr always pt to first item that u insert so it remains unchanged
            if self.__rootptr == nullpointer:
                self.__rootptr = 1 #same as newnodeptr
            else:
            #if not the first time u insert data then u need to change the ptr of the node to pt to the node that contains ur newdata
                #cur is current
                cur = self.__rootptr
                #once cur == nullptr that means u cannot go any further as u alr reach the leaf node
                while cur != nullpointer:
                    #cuz cur gonna change value later so prev is actually the initial value of cur
                    prev = cur
                    if newitem < self.__tree[cur].getdata():
                        turnedleft = True
                        #cur is now index of node u r gg towards
                        cur = self.__tree[cur].getleft()
                    else:
                        turnedleft = False
                        cur = self.__tree[cur].getright()


                #once cur pts to null then u reach the leaf node 
                if turnedleft == True:
                    #once u insert the new node the node b4 (called prev) it was orginally the leaf node 
                    self.__tree[prev].setleft(newnodeptr)
                else:

                    self.__tree[prev].setright(newnodeptr)
        else:
            print('No free node available')

    def find(self,searchitem):
        cur = self.__rootptr
        while cur!=nullpointer and self.__tree[cur].getdata() != searchitem:
            if searchitem < self.__tree[cur].getdata():
                cur = self.__tree[cur].getleft()
            else:
                cur = self.__tree[cur].getright()
        #prints index of data
        if cur==nullpointer: 
            print ('data not found')
        elif self.__tree[cur].getdata() == searchitem:
            print ('data is at index {}'.format(cur))
            
    def preorder(self,index):
        if index != nullpointer:
            print(self.__tree[index].getdata())
            self.preorder(self.__tree[index].getleft()) 
            self.preorder(self.__tree[index].getright())
            
    def inorder(self,index):
        if index != nullpointer:
            #inorder is a func so dunnid __inorder
            self.inorder(self.__tree[index].getleft())
            print(self.__tree[index].getdata())
            self.inorder(self.__tree[index].getright())

    def postorder(self,index):
        if index != nullpointer:
            self.postorder(self.__tree[index].getleft()) 
            self.postorder(self.__tree[index].getright())
            print(self.__tree[index].getdata())
    
    def getrootptr(self):
        return self.__rootptr

def main():
    bst = BST()
##    bst.insert('B')
##    bst.insert('C')
##    bst.insert('A')
    bst.display()
    bst.insert('Durian')
    bst.insert('Orange')
    bst.insert('Apple')
    bst.display()
    bst.insert('Honeydew')
    bst.insert('Banana')
    bst.display()
    bst.find('spencer')
    bst.find('Apple')
    bst.inorder(bst.getrootptr())
    
    #i.e rootptr is always 1 but if u use deletion then rootptr changes but deletion
    #not in syllabus so just assume root ptr is always 1 (if u start from index 1)
    #cannot bst.__rootpointer this is private attribute can only be accessed in a class so need create
    #public method to access it 

main()
    

    
