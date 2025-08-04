def alternateSort(arr):
    n = len(arr)
    arr.sort()
    i = 0
    j = n-1
    result = []
    while j>i:
        result.append(arr[j])
        result.append(arr[i])
        j-=1
        i+=1
    if n%2 != 0:
        result.append(arr[i])
    return result
arr = list(map(int,input().split()))
print(alternateSort(arr))
