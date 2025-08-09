arr = list(map(int,input().split()))
n = len(arr)
for i in range(n-1):
    arr[i] = arr[i] ^ arr[i+1]
print(arr)
