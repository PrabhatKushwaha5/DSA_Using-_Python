nums = [1,3,6,7]
n = 4
minn = float("inf")
for i in nums:
    minn = min(i-n,minn)
    ans = minn
print(i)