def firstOccurance(arr, num):
    l = 0
    h = len(arr)-1
    m = (l+h)//2
    if arr[m] == num:
        if arr[m-1] == num:
            return firstOccurance(arr[:m+1], num)
        else:
            return m
    elif arr[m] < num:
        return m + firstOccurance(arr[m:], num)
    else:
        return firstOccurance(arr[:m], num)
        
        
def lastOccurance(arr, num):
    l = 0
    h = len(arr)-1
    m = (l+h)//2
    if arr[m] == num:
        if arr[m+1] == num:
            return m + lastOccurance(arr[m:], num)
        else:
            return m
    elif arr[m] < num:
        return m + lastOccurance(arr[m:], num)
    else:
        return lastOccurance(arr[:m], num)


arr = [2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 10]
num = 7    
ans = firstOccurance(arr, num)
print(ans) # prints 5 

arr = [2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 10]
num = 7
ans = lastOccurance(arr, num)
print(ans) # prints 19
