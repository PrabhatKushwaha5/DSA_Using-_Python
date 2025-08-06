nums = list(map(int, input().split()))
n = len(nums)
last_smaller = float("-inf")
nums.sort()
count = 0
longest = 0  

for i in range(n):
    num = nums[i]
    if num - 1 == last_smaller:
        count += 1
        last_smaller = num
    elif num != last_smaller:
        count = 1
        last_smaller = num
    longest = max(longest, count)  
print(longest)
