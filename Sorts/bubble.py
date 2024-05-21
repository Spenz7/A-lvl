def bsort(arr):
    for i in range(len(arr)):
        #after inner for loop is done last element is sorted alr
        #-i is optional to omit last/last few elements cuz its sorted
        for i in range(len(arr)-1-i):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1], = arr[i+1],arr[i]
        #print(arr)
    return arr




arr = [9,4,8,2,7,3,6,1,5]
print(bsort(arr))


#can sort 2d lists
a = ['5','spencer']
b = ['1','john']
if a>b:
    print('true')

x = [['5','spencer'],['1','john']]
print(bsort(x))
