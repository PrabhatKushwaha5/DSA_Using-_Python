def upper_bound(nums, target):
    n = len(nums)
    ub = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:   
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub



nums = [1, 3, 5, 7, 9, 11]
target = 7

print(upper_bound(nums, target)) 
