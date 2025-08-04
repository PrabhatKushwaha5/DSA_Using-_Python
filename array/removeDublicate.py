def removeduplicate(arr):
    n = len(arr)
    if n==1:
        return 1
     
    i = 0
    j = 1
    while j<n:
        if arr[j] != arr[i]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1
    return i+1

arr = list(map(int,input().split()))
removed_duplicate = removeduplicate(arr)
print(removed_duplicate)