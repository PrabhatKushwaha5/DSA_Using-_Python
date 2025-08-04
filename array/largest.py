def largest(nums):
    largest_value = float("-inf")
    n = len(nums)
    for i in range(0,n):
        largest_value = max(largest_value,nums[i])
    return largest_value

nums = list(map(int,input().split()))
print(largest(nums))