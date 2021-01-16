# Binary Search Iterative
def binarySearch(arr, num):
    
    start = 0
    end = len(arr) - 1
    # mid = (start+end)//2
    while start<=end:
        mid = ( start + end ) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid
        else:
            start = mid
            
    return -1
    
    
# Binary Search Recursive
def binarySearchRecursive(arr, num):
    start = 0
    end = len(arr) - 1
    
    mid = ( start + end ) // 2
    
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return binarySearchRecursive(arr[:mid], num)
    else:
        return mid + binarySearchRecursive(arr[mid:], num)
        
        
arr = [1, 2, 4, 5, 6, 7, 8, 9, 20, 23, 24, 25, 26, 27, 28, 30, 34, 36, 37, 38, 45, 46, 47]
print(binarySearch(arr, 4))
print(binarySearchRecursive(arr, 4))
