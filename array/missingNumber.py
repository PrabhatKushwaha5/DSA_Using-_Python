"""nums = list(map(int,input().split()))
n = len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)
        """


#optimal Solution

nums = list(map(int,input().split()))
n = len(nums)
freq={}
for i in range(0,n+1):
    freq[i] = 0
for num in nums:
    freq[num] = 1
for k,v in freq.items():
    if v == 0:
        print(k)