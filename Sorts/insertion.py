def insertion_sort(arr):
    #n is last index 
    n = len(arr) - 1
    #i is current pos of element
    i = 0
    #n-1 cuz last comparism is i = n-1 so compare n-1 with n
    
    while i <= (n - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i + 1]
            j = i

            while (j >= 0 and arr[j] > temp):
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = temp
    
        i += 1


    return arr

arr = [9,4,8,2]
print(insertion_sort(arr))
