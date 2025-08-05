arr = list(map(int,input().split()))
n = len(arr)
freq = {}
for i in range(0,n):
    if arr[i] not in freq:
        freq[arr[i]] = 0
    freq[arr[i]] += 1
for k,v in freq.items():
    if v == 1:
        print(k)
                