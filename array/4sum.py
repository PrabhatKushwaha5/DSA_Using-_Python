def foursum(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates for i
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicates for j
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k - 1]:  # skip duplicates for k
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:  # skip duplicates for l
                        l -= 1

                elif total < target:
                    k += 1
                else:
                    l -= 1

    return ans


# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(foursum(nums, target))
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
