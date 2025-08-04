t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int,input().split()))
    data = []
    for i in range(n-1,-1,-1):
        data.append(ar[i])
    
    if data[::] == ar[::]:
        print("Yes")
        