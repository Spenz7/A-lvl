def Quicksort(array, first, last):
    #u dw change val of first and last so u store in start and end
    start = first
    end = last
    mid = arr[(first + last) // 2]
    
    while start <= end:

        #scan from left till an out of order element is found
        while array[start] < mid:
            start = start + 1

        #scan from right till an out of order element is found
        while array[end] > mid:
            end = end - 1

        if start <= end:
            
            array[start],array[end] = array[end],array[start]
            start = start + 1
            end = end - 1

    

    #if first is to the left of end
    if first < end:
        Quicksort(array, first, end)

    #if last is to the right of start
    if start < last:
        Quicksort(array, start, last)

    return array

arr = [78, 46, 35, 5, 20, 16, 1, 87, 41, 11]
print(Quicksort(arr,0,len(arr)-1))
            
arr = [9,4,8,2,7,3,6,1,5]
print(Quicksort(arr,0,len(arr)-1))
