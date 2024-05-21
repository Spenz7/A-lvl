def qsort(arr):
    if len(arr)<=1:
        return arr
    #pivot is an actual array value
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]

    return qsort(left)+middle+qsort(right)

arr = [9,4,8,2,7,3,6,1,5]
print(qsort(arr))
