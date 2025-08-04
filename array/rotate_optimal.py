def rotateOptimal(arr,k):
    n = len(arr)
    rotateBy = k%n
    for _ in range(0,rotateBy):
        e = arr.pop()
        arr.insert(0,e)

arr = list(map(int,input().split()))
k = int(input())
rotateOptimal(arr,k)
print(arr)