def isort(arr):
    #get last index of array
    n = len(arr)-1
    #start comparing from index 0
    i = 0

    while i<=(n-1):
        if arr[i]>arr[i+1]:
            #prepare for backward scan
            temp = arr[i+1]
            #j is index of first left element u compare with
            #inner loop initialise to same value as outer loop
            j = i

        #while loop for backward scan is inside the if 
        #or j!=-1
            while (j>=0 and arr[j]>temp):
                
                arr[j+1] = arr[j]
                j = j-1

            #when j is -1 or arr[j]<= temp
            arr[j+1] = temp   

        #increase i by 1
        i = i+1

    return arr

arr = [9,4,8]
print(isort(arr))


#eg arr = [1,2,3,5,4] so u store 4 in temp and start backward scan from 5,
#i.e 3<4 so insert 4 at where 5 is, then insert 5 where 4 initially was
