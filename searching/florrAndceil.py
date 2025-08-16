def floorAndCeil(target, nums):
    n = len(nums)
    floor = -1
    ceil = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:  # nums[mid] < target
            floor = nums[mid]
            low = mid + 1

    return [floor, ceil]


# Example usage
target = int(input("Enter target: "))
nums = list(map(int, input("Enter sorted array: ").split()))
print(floorAndCeil(target, nums))
