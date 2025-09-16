def secondLargest(n):
    n.sort()
    return n[-2]

n = list(map(int,input().split()))
print(secondLargest(n))