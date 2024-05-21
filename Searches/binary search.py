
# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch (arr, left, right, x):
    
    # Check base case
    
    
    if right >= left:
        
        mid = (left + right) // 2
        
        # If element is present at the middle itself
        if arr[mid] == x:
            print(mid)
            return mid
        
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, left, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            #imagine an array u hold right ptr in place at last element
            #while u shift left ptr 4ward by 1
            return binarySearch(arr, mid + 1, right, x)

    else:
        # Element is not present in the array
        return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 70

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
