def binarySearch(nums, low, high, target):
    
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, high, target)
    else:
        return binarySearch(nums, low, mid - 1, target)



if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    result = binarySearch(nums, 0, len(nums) - 1, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
