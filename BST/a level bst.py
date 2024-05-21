
class node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.data = ''
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getdata(self):
        return self.data
    def setleft(self,new):
        self.left = new
    def setright(self,new):
        self.right = new
    def setdata(self,new):
        self.data = new

class BST:
    
    def __init__(self,size):
        self.size = size
        self.root = -1
        self.nextfree = 0
        self.bst = [node() for i in range(size)]
        for i in range(len(self.bst)-1):
            self.bst[i].setleft(i+1)

    def display(self):
        
        print('{:^10}|{:^10}|{:^10}|{:^10}'.format('index','left','data','right'))
        for i in range(len(self.bst)):
            print('{:^10}|{:^10}|{:^10}|{:^10}'.format(i,self.bst[i].getleft(),self.bst[i].getdata(),self.bst[i].getright()))
        print('self.root = ',self.root)
        print('self.nextfree = ',self.nextfree)
        
        
    def insert(self,new):
        if self.nextfree == -1:
            return 'full'
        #NEED STORE self.nextfree in temp cuz u gonna change self.nextfree later
        temp = self.nextfree
        #must set left to -1 cuz left !=-1 when u init bst
        self.nextfree = self.bst[self.nextfree].getleft()
        self.bst[temp].setdata(new)
        self.bst[temp].setleft(-1)
        
        
        #check if 1st time insert new data
        if self.root == -1:
            self.root = 0
        else:
            #traverse thru bst, imagine starting at root
            current = self.root
            while current != -1:
                prev = current
                #only need turnedleft
                if new<self.bst[current].getdata():
                    turnedleft = True
                    current = self.bst[current].getleft()
                else:
                    turnedleft = False
                    current = self.bst[current].getright()
                
            #once reach leaf node, pt 
            if turnedleft == True:
                self.bst[prev].setleft(temp)
            else:
                self.bst[prev].setright(temp)

    def find(self,data):
        current = self.root
        while current!=-1 and self.bst[current].getdata()!=data:
            if data<self.bst[current].getdata():
                current = self.bst[current].getleft()
            else:
                current = self.bst[current].getright()
            if current == -1:
                print('not found')
            #acc for what index its at
            else:
                print('found at index {}'.format(current))

    def inorder(self,index):
        
        if index!=-1:
            #left,data,right
            self.inorder(self.bst[index].getleft())
            print(self.bst[index].getdata())
            self.inorder(self.bst[index].getright())
        

    def getroot(self):
        return self.root
        
        
        
def main():
    bst = BST(7)
##    bst.insert('B')
##    bst.insert('C')
##    bst.insert('A')
    bst.display()
    bst.insert('Durian')
    bst.display()
    bst.insert('Orange')
    bst.display()
    bst.insert('Apple')
    bst.display()
    bst.insert('Honeydew')
    #error
    bst.display()
    bst.insert('Banana')
    bst.display()
    bst.find('spencer')
    bst.find('Apple')
    bst.inorder(bst.getroot())

main()


            
    
