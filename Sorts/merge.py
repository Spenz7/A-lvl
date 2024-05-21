#this one dunnid declare fixed array size its dynamic 
def merge(A,B):
    merged = []
    #non-zero is true, rmb 0 is false and true is 1 its while len(A) =1
    while len(A) and len(B):
        print('hi')
        '''use < for ascending, > for descending'''
        if A[0]<B[0]:
            print('hello')
            #A.pop(0) returns item that u popped, removes index 0 from A
            merged.append(A.pop(0))
        else:
            merged.append(B.pop(0))
    if len(A) == 0:
        merged += B
    else:
        merged += A
    return merged

#this keeps splitting array into 2 
def split(L):
    if len(L)<2:
        #return L so later its stored in left and right and u pass them as parameters into merge()
        return L
    mid = len(L)//2
    #imagine array of 8
    left = split(L[:mid])
    right = split(L[mid:])
    #once len(L) is 1 then u do line below
    return merge(left,right)

L = [5,4,3,2]
x = split(L)
print(x)
