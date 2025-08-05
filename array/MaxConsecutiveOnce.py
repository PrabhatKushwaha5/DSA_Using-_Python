nums = list(map(int,input().split()))
n = len(nums)
count = 0
max_c = 0
for i in range(n):
    if nums[i] == 1:
        count += 1
    else:
        max_c = max(count,max_c)
        count = 0
print(max(count,max_c))