def upperBound(arr, n, x):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] <= x:
            
            low = mid + 1
        else:
            
            high = mid - 1

    return low


# ---------- INPUT / OUTPUT ----------
n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(upperBound(arr, n, x))
