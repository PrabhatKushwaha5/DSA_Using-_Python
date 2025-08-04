#it is a brute force method

nums = list(map(int,input().split()))
k = int(input())
for _ in range(0,k):
    e = nums.pop()
    nums.insert(0,e)
print(nums)