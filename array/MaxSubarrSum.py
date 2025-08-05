nums = list(map(int,input().split()))
n = len(nums)
maxi = float("-inf")
total = 0
for i in range(0,n):
    total = total+nums[i]
    maxi = max(total,maxi)
    if total < 0:
        total = 0
print(maxi)