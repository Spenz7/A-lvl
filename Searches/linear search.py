#linear search
arr = [9,4,8,2,7,3,6,1,5]



def find(tofind):
    for i in range(len(arr)):
        if arr[i] == tofind:
            return('found at index {}'.format(i))
            
    return('not found')

print(find(5))
