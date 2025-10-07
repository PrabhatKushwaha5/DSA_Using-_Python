class Solution(object):
    def search(self, nums, target):  # added 'self'
        n = len(nums)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


nums = list(map(int, input().split()))
target = int(input())

sol = Solution()
print(sol.search(nums, target))
