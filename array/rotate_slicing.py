# left rotate

nums = list(map(int,input().split()))
k = int(input())
n = len(nums)
d = k%n
nums[:] = nums[d:] + nums[:d]
print(nums)