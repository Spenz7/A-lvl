class hashtable:
    def __init__(self,limit):
        self.limit = limit
        self.table = ['' for i in range(self.limit)]
        
    def display(self):
        print('{:^10}|{:^10}'.format('index','data'))
        for i in range(self.limit):
            print('{:^10}|{:^10}'.format(i,self.table[i]))

    def hashfunc(self,data):
        total = 0
        for i in data:
            total+=ord(i)
        index = total%self.limit
        return index

    #if collison occurs
    '''rehash fn takes in oldindex'''
    def rehash(self,index):
        return (index+1)%self.limit

    def insert(self,data):
        index = self.hashfunc(data)
        if self.table[index] == '' or self.table[index] == 'X':
            self.table[index] = data
        else:
            newindex = self.rehash(index)
            #can reuse deleted slot
            while self.table[newindex] != '' and self.table[newindex] != 'X':
                
                '''REHASH NEWINDEX'''
                newindex = self.rehash(newindex)
            if count == self.limit:
                print('no space')
            self.table[newindex] = data
            

    def delete(self,data):
        index = self.hashfunc(data)
        if self.table[index] == data:
            #use 'X' as tombstone to indicate that its been deleted
            self.table[index] = 'X'
        else:
            newindex = self.rehash(index)
            '''counter to go thru entire list'''
            count = 0
            #if break its due to 1 of these 2 cond being false
            #imagine 5 fingers u start at index 1(2nd finger) and eachh time u move
            #to the next finger u increase count by 1, so 5 times
            '''if wan check thru every element in list count==self.limit'''
            while self.table[newindex]!=data and count!=self.limit:
                
                newindex = self.rehash(newindex)
                count+=1
            if count!=self.limit:
                self.table[newindex] = 'X'
            else:
                print(data, 'not found')

    def search(self,data):
        index = self.hashfunc(data)
        if self.table[index] == data:
            print('data found at index: ',index)
        else:
            newindex = self.rehash(index)
            #cuz initially u check 0 times
            count = 0
            while self.table[newindex]!=data and count!=self.limit:
                newindex = self.rehash(newindex)
                #when move onto next index increment count by 1
                count+=1
            if count!=0:
                print('found at index ', newindex)
            else:
                print('not found')
                
        
        

def main():
    h1 = hashtable(11)
    #print(h1.hashfunc('B7MF'))
    h1.insert('apple')
    
    h1.insert('orange')
    
    h1.insert('durian')
    
    h1.insert('A5RD')
    
    h1.insert('B7MF')
    
    
    h1.insert('B7MF')
    
    h1.display()
    print('\n')
    h1.delete('B7MF')
    h1.display()

    h1.search('B7MF')
    h1.display()
    h1.search('A5RD')
    h1.search('B7MF')
    h1.insert('orange')
    print('\n')


main()
